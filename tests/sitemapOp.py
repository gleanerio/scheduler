import os, json, io
import urllib
from urllib import request
from dagster import job, op, get_dagster_logger, schedule
from minio import Minio
from minio.error import S3Error
from datetime import datetime
from urllib.request import urlopen
import advertools as adv
import requests, sys, os
import yaml, yaql
from urllib.request import urlopen
import urllib.request
import logging
import argparse
from typing import Tuple
import pandas as pd

NAME = "sitemapcheck"

# env items
URL = os.environ.get('PORTAINER_URL')
APIKEY = os.environ.get('PORTAINER_KEY')
IMAGE = os.environ.get('GLEANERIO_IMAGE')
ARCHIVE_FILE = os.environ.get('GLEANERIO_ARCHIVE_FILE')
ARCHIVE_PATH = os.environ.get('GLEANERIO_ARCHIVE_PATH')
MINIO_URL = os.environ.get('GLEANER_MINIO_URL')
MINIO_SECRET = os.environ.get('GLEANER_MINIO_SECRET')
MINIO_KEY = os.environ.get('GLEANER_MINIO_KEY')
MINIO_BUCKET = os.environ.get('GLEANER_MINIO_BUCKET')

def s3reader():
    server = os.environ.get('GLEANER_MINIO_URL') + ":" + os.environ.get('GLEANER_MINIO_PORT')
    client = Minio(
        server,
        secure=False,
        access_key=os.environ.get('GLEANER_MINIO_KEY'),
        secret_key=os.environ.get('GLEANER_MINIO_SECRET'),
    )
    try:
        data = client.get_object(os.environ.get('GLEANER_MINIO_BUCKET'), os.environ.get('GLEANERIO_ARCHIVE_OBJECT'))
        return data
    except S3Error as err:
        get_dagster_logger().info(f"S3 read error : {str(err)}")

def s3loader(data):
    server = os.environ.get('GLEANER_MINIO_URL') + ":" + os.environ.get('GLEANER_MINIO_PORT')
    client = Minio(
        server,
        secure=False,
        access_key=os.environ.get('GLEANER_MINIO_KEY'),
        secret_key=os.environ.get('GLEANER_MINIO_SECRET'),
    )

    # Make 'X' bucket if not exist.
    # found = client.bucket_exists("X")
    # if not found:
    #     client.make_bucket("X")
    # else:
    #     print("Bucket 'X' already exists")

    now = datetime.now()
    date_string = now.strftime("%Y_%m_%d_%H_%M_%S")

    logname = NAME + '_{}.log'.format(date_string)
    objPrefix = os.environ.get('GLEANERIO_LOG_PREFIX')+logname
    client.put_object(os.environ.get('GLEANER_MINIO_BUCKET'),
                      objPrefix,
                      io.BytesIO(data),
                      len(data))
    get_dagster_logger().info(f"Log uploaded: {str(objPrefix)}")

def check_sitemapv2(smurl, stype, name: str) -> Tuple[int, str]:
    logging.getLogger('requests').setLevel(logging.ERROR)  # 'NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    logging.getLogger('advertools').setLevel(logging.ERROR)

    if stype == "sitegraph":
        x = requests.head(smurl)
        if x.status_code == 404:  # could check for 200 or 303?
            res = str("ERROR {} : {} Sitegrap URL is 404".format(name, smurl))
            return 1, res  # sys.exit(os.EX_SOFTWARE)
        else:
            res = str("{} \t {} Sitegraph URL code is {} ".format(name, smurl, x.status_code))
            return 0, res  # sys.exit(os.EX_OK)
    else:
        try:
            r = requests.get(smurl)
        except:
            res = str("ERROR making request, no further information at this time")
            return 1, res
        if r.status_code == 404:
            res = str("ERROR {} : {} Sitemap URL is 404".format(name, smurl))
            return 1, res  # sys.exit(os.EX_SOFTWARE)
        else:
            try:
                iow_sitemap = adv.sitemap_to_df(smurl)
                usm = iow_sitemap.sitemap.unique()
                uloc = iow_sitemap["loc"].unique()
                res = str("{} : {} VALID {}  with {} sitemap URL(s)".format(len(uloc), name, smurl, len(usm)))
                return 0, res  # sys.exit(os.EX_OK)
            except:
                res = str("ERROR {} : {} reading sitemap XML".format(name, smurl))
                return 1, res

@op
def sitemaptest():
    # sources = '/home/fils/src/Projects/gleaner.io/scheduler/dagster/dagster-docker/src/implnet-eco/gleanerconfig.yaml'
    sources = s3reader()
    data_source = yaml.safe_load(sources)

    rl = []
    for s in data_source["sources"]:
        url = s["url"]
        stype = s["sourcetype"]
        name = s["name"]

        r, res = check_sitemapv2(url, stype, name)

        data = {'name': name, 'code': r, 'description': res, 'url': url, 'type': stype}
        rl.append(data)

    # leverage pandas to convert to csv
    df = pd.DataFrame.from_dict(rl)
    csv_data = df.to_csv(index=False)

    s3loader(str(csv_data).encode())  # s3loader needs a bytes like object

    get_dagster_logger().info(f"CSV: {str(csv_data)}")

@job
def implnet_job_sitemap():
    sitemaptest()

# 0 3 * * *   is at 3 AM each day
@schedule(cron_schedule="0 3 * * *", job=implnet_job_sitemap, execution_timezone="US/Central")
def implnet_sch_sitemap(_context):
        run_config = {}
        return run_config
