import json
import os

import pandas as pd
from dagster import asset, get_dagster_logger
from ec.datastore import s3

GLEANER_MINIO_ADDRESS = os.environ.get('GLEANERIO_MINIO_ADDRESS')
GLEANER_MINIO_PORT = os.environ.get('GLEANERIO_MINIO_PORT')
GLEANER_MINIO_USE_SSL = os.environ.get('GLEANERIO_MINIO_USE_SSL')
GLEANER_MINIO_SECRET_KEY = os.environ.get('GLEANERIO_MINIO_SECRET_KEY')
GLEANER_MINIO_ACCESS_KEY = os.environ.get('GLEANERIO_MINIO_ACCESS_KEY')
GLEANER_MINIO_BUCKET = os.environ.get('GLEANERIO_MINIO_BUCKET')

REPORT_PATH = "reports/"
ORG_PATH = "orgs/"
STAT_FILE_NAME = "missing_report_graph.json"
def _pythonMinioUrl(url):

    if (url.endswith(".amazonaws.com")):
        PYTHON_MINIO_URL = "s3.amazonaws.com"
    else:
        PYTHON_MINIO_URL = url
    return PYTHON_MINIO_URL

def getName(name):
    return name.replace("orgs/","").replace(".nq","")
@asset()
def source_list() -> None:
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    orglist = s3Minio.listPath(GLEANER_MINIO_BUCKET, ORG_PATH,recursive=False)
    sources = map( lambda f: { "name": getName(f.object_name)}, orglist )

    os.makedirs("data", exist_ok=True)


    with open("data/source_list.json", "w") as f:
        json.dump(list(sources), f)
#@asset(deps=[source_list])
@asset(deps=[source_list])
def loadstats() -> None:
    logger = get_dagster_logger()
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
 #   sourcelist = list(s3Minio.listPath(GLEANER_MINIO_BUCKET, ORG_PATH,recursive=False))

    with open("data/source_list.json","r" ) as f:
        sourcelist = json.load(f)
    stats = []
    for source in sourcelist:
        try:
            stat = s3Minio.getReportFile(GLEANER_MINIO_BUCKET,source.get("name"), STAT_FILE_NAME )
            stat = json.loads(stat)
            stats.append(stat)
        except:
            logger.info(f"Failed to get { source.get('name')} ")
    df = pd.DataFrame(stats)
    df.to_csv("data/weekly_stats.csv")
