import distutils

from dagster import op, graph, get_dagster_logger
import subprocess
import os, json, io
import urllib
from urllib import request
from dagster import job, op, get_dagster_logger
from ec.gleanerio.gleaner import getGleaner, getSitemapSourcesFromGleaner
from minio import Minio
from minio.error import S3Error
from datetime import datetime
from ec.reporting.report import missingReport, generateGraphReportsRepo
from ec.datastore import s3
from ec.graph.manageGraph import ManageBlazegraph as mg

import requests
import logging as log

from requests import HTTPError
from ec.reporting.report import missingReport
from ec.datastore import s3

# Vars and Envs

# env items
URL = os.environ.get('PORTAINER_URL')
APIKEY = os.environ.get('PORTAINER_KEY')

def _pythonMinioUrl(url):
    if (url.endswith(".amazonaws.com")):
        PYTHON_MINIO_URL = "s3.amazonaws.com"
    else:
        PYTHON_MINIO_URL = url
    return PYTHON_MINIO_URL

GLEANER_MINIO_ADDRESS = os.environ.get('GLEANER_MINIO_ADDRESS')
GLEANER_MINIO_PORT = os.environ.get('GLEANER_MINIO_PORT')
GLEANER_MINIO_USE_SSL = os.environ.get('GLEANER_MINIO_USE_SSL')
GLEANER_MINIO_SECRET_KEY = os.environ.get('GLEANER_MINIO_SECRET_KEY')
GLEANER_MINIO_ACCESS_KEY = os.environ.get('GLEANER_MINIO_ACCESS_KEY')
GLEANER_MINIO_BUCKET = os.environ.get('GLEANER_MINIO_BUCKET')
GLEANER_HEADLESS_ENDPOINT = os.environ.get('GLEANER_HEADLESS_ENDPOINT')
# using GLEANER, even though this is a nabu property... same prefix seems easier
GLEANER_GRAPH_URL = os.environ.get('GLEANER_GRAPH_URL')
GLEANER_GRAPH_NAMESPACE = os.environ.get('GLEANER_GRAPH_NAMESPACE')

def postRelease(source):
    # revision of EC utilities, will have a insertFromURL
    #instance =  mg.ManageBlazegraph(os.environ.get('GLEANER_GRAPH_URL'),os.environ.get('GLEANER_GRAPH_NAMESPACE') )
    proto = "http"

    if os.environ.get('GLEANER_MINIO_USE_SSL'):
        proto = "https"
    port = os.environ.get('GLEANER_MINIO_PORT')
    address = os.environ.get('GLEANER_MINIO_ADDRESS')
    bucket = os.environ.get('GLEANER_MINIO_BUCKET')
    path = "graphs/latest"
    release_url = f"{proto}://{address}:{port}/{bucket}/{path}/{source}_release.nq"
    url = f"{os.environ.get('GLEANER_GRAPH_URL')}/namespace/{os.environ.get('GLEANER_GRAPH_NAMESPACE')}/sparql?uri={release_url}"
    log.info(f'insert "{source}" to {url} ')

    r = requests.post(url)
    log.debug(f' status:{r.status_code}')  # status:404
    log.info(f' status:{r.status_code}')  # status:404
    if r.status_code == 200:
        # '<?xml version="1.0"?><data modified="0" milliseconds="7"/>'
        if 'data modified="0"' in r.text:
            raise Exception("No Data Added: " + r.text)
        return True
    else:
        return False

def _pythonMinioUrl(url):

    if (url.endswith(".amazonaws.com")):
        PYTHON_MINIO_URL = "s3.amazonaws.com"
    else:
        PYTHON_MINIO_URL = url
    return PYTHON_MINIO_URL
def read_file_bytestream(image_path):
    data = open(image_path, 'rb').read()
    return data


def load_data(file_or_url):
    try:
        with urllib.request.urlopen(file_or_url) as f:
            data = f.read()
    except ValueError:
        with open(file_or_url, 'rb') as f:
            data = f.read()
    return data


def s3reader(object):
    server =  _pythonMinioUrl(os.environ.get('GLEANER_MINIO_ADDRESS')) + ":" + os.environ.get('GLEANER_MINIO_PORT')
    get_dagster_logger().info(f"S3 URL    : {str(os.environ.get('GLEANER_MINIO_ADDRESS'))}")
    get_dagster_logger().info(f"S3 PYTHON SERVER : {server}")
    get_dagster_logger().info(f"S3 PORT   : {str(os.environ.get('GLEANER_MINIO_PORT'))}")
    # get_dagster_logger().info(f"S3 read started : {str(os.environ.get('GLEANER_MINIO_KEY'))}")
    # get_dagster_logger().info(f"S3 read started : {str(os.environ.get('GLEANER_MINIO_SECRET'))}")
    get_dagster_logger().info(f"S3 BUCKET : {str(os.environ.get('GLEANER_MINIO_BUCKET'))}")
    get_dagster_logger().info(f"S3 object : {str(object)}")

    client = Minio(
        server,
        # secure=True,
        secure = bool(distutils.util.strtobool(os.environ.get('GLEANER_MINIO_USE_SSL'))),
        access_key=os.environ.get('GLEANER_MINIO_ACCESS_KEY'),
        secret_key=os.environ.get('GLEANER_MINIO_SECRET_KEY'),
    )
    try:
        data = client.get_object(os.environ.get('GLEANER_MINIO_BUCKET'), object)
        return data
    except S3Error as err:
        get_dagster_logger().info(f"S3 read error : {str(err)}")


def s3loader(data, name):
    secure= bool(distutils.util.strtobool(os.environ.get('GLEANER_MINIO_USE_SSL')))
    if (os.environ.get('GLEANER_MINIO_PORT') and os.environ.get('GLEANER_MINIO_PORT') == 80
             and secure == False):
        server = _pythonMinioUrl(os.environ.get('GLEANER_MINIO_ADDRESS'))
    elif (os.environ.get('GLEANER_MINIO_PORT') and os.environ.get('GLEANER_MINIO_PORT') == 443
                and secure == True):
        server = _pythonMinioUrl(os.environ.get('GLEANER_MINIO_ADDRESS'))
    else:
        # it's not on a normal port
        server = f"{_pythonMinioUrl(os.environ.get('GLEANER_MINIO_ADDRESS'))}:{os.environ.get('GLEANER_MINIO_PORT')}"

    client = Minio(
        server,
        secure=secure,
        #secure = bool(distutils.util.strtobool(os.environ.get('GLEANER_MINIO_SSL'))),
        access_key=os.environ.get('GLEANER_MINIO_ACCESS_KEY'),
        secret_key=os.environ.get('GLEANER_MINIO_SECRET_KEY'),
    )

    # Make 'X' bucket if not exist.
    # found = client.bucket_exists("X")
    # if not found:
    #     client.make_bucket("X")
    # else:
    #     print("Bucket 'X' already exists")

    now = datetime.now()
    date_string = now.strftime("%Y_%m_%d_%H_%M_%S")

    logname = name + '_{}.log'.format(date_string)
    objPrefix = os.environ.get('GLEANERIO_LOG_PREFIX') + logname
    f = io.BytesIO()
    #length = f.write(bytes(json_str, 'utf-8'))
    length = f.write(data)
    f.seek(0)
    client.put_object(os.environ.get('GLEANER_MINIO_BUCKET'),
                      objPrefix,
                      f, #io.BytesIO(data),
                      length, #len(data),
                      content_type="text/plain"
                         )
    get_dagster_logger().info(f"Log uploaded: {str(objPrefix)}")


def gleanerio(mode, source):
    ## ------------   Create

    get_dagster_logger().info(f"Create: {str(mode)}")

    if str(mode) == "gleaner":
        IMAGE = os.environ.get('GLEANERIO_GLEANER_IMAGE')
        ARCHIVE_FILE = os.environ.get('GLEANERIO_GLEANER_ARCHIVE_OBJECT')
        ARCHIVE_PATH = os.environ.get('GLEANERIO_GLEANER_ARCHIVE_PATH')
        CMD = ["--cfg", "/gleaner/gleanerconfig.yaml", "--source", source, "--rude"]
        NAME = "gleaner01_" + source
        # LOGFILE = 'log_gleaner.txt'  # only used for local log file writing
    elif (str(mode) == "nabu"):
        IMAGE = os.environ.get('GLEANERIO_NABU_IMAGE')
        ARCHIVE_FILE = os.environ.get('GLEANERIO_NABU_ARCHIVE_OBJECT')
        ARCHIVE_PATH = os.environ.get('GLEANERIO_NABU_ARCHIVE_PATH')
        CMD = ["--cfg", "/nabu/nabuconfig.yaml", "prune", "--prefix", "summoned/" + source]
        NAME = "nabu01_" + source
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
    elif (str(mode) == "prov"):
        IMAGE = os.environ.get('GLEANERIO_NABU_IMAGE')
        ARCHIVE_FILE = os.environ.get('GLEANERIO_NABU_ARCHIVE_OBJECT')
        ARCHIVE_PATH = os.environ.get('GLEANERIO_NABU_ARCHIVE_PATH')
        CMD = ["--cfg", "/nabu/nabuconfig.yaml", "prefix", "--prefix", "prov/" + source]
        NAME = "nabu01_" + source
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
    elif (str(mode) == "orgs"):
        IMAGE = os.environ.get('GLEANERIO_NABU_IMAGE')
        ARCHIVE_FILE = os.environ.get('GLEANERIO_NABU_ARCHIVE_OBJECT')
        ARCHIVE_PATH = os.environ.get('GLEANERIO_NABU_ARCHIVE_PATH')
        CMD = ["--cfg", "/nabu/nabuconfig.yaml", "prefix", "--prefix", "orgs"]
        NAME = "nabu01_" + source
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
    elif (str(mode) == "release"):
        IMAGE = os.environ.get('GLEANERIO_NABU_IMAGE')
        ARCHIVE_FILE = os.environ.get('GLEANERIO_NABU_ARCHIVE_OBJECT')
        ARCHIVE_PATH = os.environ.get('GLEANERIO_NABU_ARCHIVE_PATH')
        CMD = ["--cfg", "/nabu/nabuconfig.yaml", "release", "--prefix", "summoned/" + source]
        NAME = "nabu01_" + source
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
    else:
        return 1

    data = {}
    data["Image"] = IMAGE
    data["Cmd"] = CMD

    # add in env variables here"Env": ["FOO=bar","BAZ=quux"],
    enva = []
    enva.append(str("MINIO_ADDRESS={}".format(GLEANER_MINIO_ADDRESS)))
    enva.append(str("GLEANER_MINIO_PORT={}".format(GLEANER_MINIO_PORT)))
    enva.append(str("MINIO_USE_SSL={}".format(GLEANER_MINIO_USE_SSL)))
    enva.append(str("MINIO_SECRET_KEY={}".format(GLEANER_MINIO_SECRET_KEY)))
    enva.append(str("MINIO_ACCESS_KEY={}".format(GLEANER_MINIO_ACCESS_KEY)))
    enva.append(str("GLEANER_MINIO_BUCKET={}".format(GLEANER_MINIO_BUCKET)))
    enva.append(str("GLEANER_HEADLESS_ENDPOINT={}".format(os.environ.get('GLEANER_HEADLESS_ENDPOINT'))))

    data["Env"] = enva
    try:
        url = URL + 'containers/create'
        params = {
            "name": NAME
        }
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        get_dagster_logger().info(f"URL: {str(url)}")

        req = request.Request(url, str.encode(json.dumps(data)))
        req.add_header('X-API-Key', APIKEY)
        req.add_header('content-type', 'application/json')
        req.add_header('accept', 'application/json')
        try:
            r = request.urlopen(req)
            c = r.read()
            d = json.loads(c)
            cid = d['Id']
            print(r.status)
            get_dagster_logger().info(f"Create: {str(r.status)}")
        except HTTPError as err:
            if (err.code == 409):
                print("failed to create container: container exists; use docker container ls -a : ", err)
                get_dagster_logger().info(f"Create Failed: exsting container:  container exists; use docker container ls -a : {str(err)}")
            elif (err.code == 404):
                print("failed to create container: missing GLEANER_CONTAINER_IMAGE: load into portainer/docker : ", err)
                get_dagster_logger().info(f"Create Failed: bad GLEANER_CONTAINER_IMAGE: load into portainer/docker : reason {str(err)}")
            else:
                print("failed to create container:  unknown reason: ", err)
                get_dagster_logger().info(f"Create Failed: unknown reason {str(err)}")
            raise err

        # print(cid)

        ## ------------  Archive to load, which is how to send in the config (from where?)

        url = URL + 'containers/' + cid + '/archive'
        params = {
            'path': ARCHIVE_PATH
        }
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        # print(url)

        # DATA = read_file_bytestream(ARCHIVE_FILE)
        DATA = s3reader(ARCHIVE_FILE)

        req = request.Request(url, data=DATA, method="PUT")
        req.add_header('X-API-Key', APIKEY)
        req.add_header('content-type', 'application/x-compressed')
        req.add_header('accept', 'application/json')
        r = request.urlopen(req)

        print(r.status)
        get_dagster_logger().info(f"Archive: {str(r.status)}")

        # c = r.read()
        # print(c)
        # d = json.loads(c)
        # print(d)

        ## ------------  Start

        url = URL + 'containers/' + cid + '/start'
        req = request.Request(url, method="POST")
        req.add_header('X-API-Key', APIKEY)
        req.add_header('content-type', 'application/json')
        req.add_header('accept', 'application/json')
        r = request.urlopen(req)
        print(r.status)
        get_dagster_logger().info(f"Start: {str(r.status)}")

        ## ------------  Wait expect 200

        url = URL + 'containers/' + cid + '/wait'
        req = request.Request(url, method="POST")
        req.add_header('X-API-Key', APIKEY)
        req.add_header('content-type', 'application/json')
        req.add_header('accept', 'application/json')
        r = request.urlopen(req)
        print(r.status)
        get_dagster_logger().info(f"Wait: {str(r.status)}")

        ## ------------  Copy logs  expect 200

        url = URL + 'containers/' + cid + '/logs'
        params = {
            'stdout': 'true',
            'stderr': 'false'
        }
        query_string = urllib.parse.urlencode(params)

        url = url + "?" + query_string
        req = request.Request(url, method="GET")
        req.add_header('X-API-Key', APIKEY)
        req.add_header('accept', 'application/json')
        r = request.urlopen(req)
        print(r.status)
        c = r.read().decode('latin-1')

        # write to file
        # f = open(LOGFILE, 'w')
        # f.write(str(c))
        # f.close()

        # write to s3

        s3loader(str(c).encode(), NAME)  # s3loader needs a bytes like object
        #s3loader(str(c).encode('utf-8'), NAME)  # s3loader needs a bytes like object
        # write to minio (would need the minio info here)

        get_dagster_logger().info(f"Logs: {str(r.status)}")

        ## ------------  Remove   expect 204
    finally:
        url = URL + 'containers/' + cid
        req = request.Request(url, method="DELETE")
        req.add_header('X-API-Key', APIKEY)
        # req.add_header('content-type', 'application/json')
        req.add_header('accept', 'application/json')
        r = request.urlopen(req)
        print(r.status)
        get_dagster_logger().info(f"Remove: {str(r.status)}")

    return 0

@op
def earthchem_gleaner(context):
    returned_value = gleanerio(("gleaner"), "earthchem")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"Gleaner notes are  {r} ")
    return r

@op
def earthchem_nabu(context, msg: str):
    returned_value = gleanerio(("nabu"), "earthchem")
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def earthchem_nabuprov(context, msg: str):
    returned_value = gleanerio(("prov"), "earthchem")
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def earthchem_nabuorg(context, msg: str):
    returned_value = gleanerio(("orgs"), "earthchem")
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def earthchem_naburelease(context, msg: str):
    returned_value = gleanerio(("release"), "earthchem")
    r = str('returned value:{}'.format(returned_value))
    return msg + r
@op
def earthchem_uploadrelease(context, msg: str):
    returned_value = postRelease("earthchem")
    r = str('returned value:{}'.format(returned_value))
    return msg + r


@op
def earthchem_missingreport_s3(context, msg: str):
    source = getSitemapSourcesFromGleaner("/scheduler/gleanerconfig.yaml", sourcename="earthchem")
    source_url = source.get('url')
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "earthchem"
    graphendpoint = None
    milled = False
    summon = True
    returned_value = missingReport(source_url, bucket, source_name, s3Minio, graphendpoint, milled=milled, summon=summon)
    r = str('returned value:{}'.format(returned_value))
    report = json.dumps(returned_value, indent=2)
    s3Minio.putReportFile(bucket, source_name, "missing_report_s3.json", report)
    return msg + r
def earthchem_missingreport_grpah(context, msg: str):
    source = getSitemapSourcesFromGleaner("/scheduler/gleanerconfig.yaml", sourcename="earthchem")
    source_url = source.get('url')
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "earthchem"

    graphendpoint = f"{os.environ.get('GLEANER_GRAPH_URL')}/namespace/{os.environ.get('GLEANER_GRAPH_NAMESPACE')}/sparql"

    milled = False
    summon = True
    returned_value = missingReport(source_url, bucket, source_name, s3Minio, graphendpoint, milled=milled, summon=summon)
    r = str('returned value:{}'.format(returned_value))
    report = json.dumps(returned_value, indent=2)

    s3Minio.putReportFile(bucket, source_name, "missing_report_graph.json", report)

    return msg + r
def earthchem_graph_reports(context, msg: str):
    source = getSitemapSourcesFromGleaner("/scheduler/gleanerconfig.yaml", sourcename="earthchem")
    #source_url = source.get('url')
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "earthchem"

    graphendpoint = f"{os.environ.get('GLEANER_GRAPH_URL')}/namespace/{os.environ.get('GLEANER_GRAPH_NAMESPACE')}/sparql"

    milled = False
    summon = True
    returned_value = generateGraphReportsRepo(source_name,  graphendpoint)
    r = str('returned value:{}'.format(returned_value))
    report = json.dumps(returned_value, indent=2)

    s3Minio.putReportFile(bucket, source_name, "missing_report_graph.json", report)

    return msg + r

#Can we simplify and use just a method. Then import these methods?
# def missingreport_s3(context, msg: str, source="earthchem"):
#
#     source= getSitemapSourcesFromGleaner("/scheduler/gleanerconfig.yaml", sourcename=source)
#     source_url = source.get('url')
#     s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
#     bucket = GLEANER_MINIO_BUCKET
#     source_name="earthchem"
#
#     graphendpoint = None
#     milled = False
#     summon = True
#     returned_value = missingReport(source_url, bucket, source_name, s3Minio, graphendpoint, milled=milled, summon=summon)
#     r = str('returned value:{}'.format(returned_value))
#     return msg + r
@graph
def harvest_earthchem():
    harvest = earthchem_gleaner()

    report1 =earthchem_missingreport_s3(harvest)
    #report1 = missingreport_s3(harvest, source="earthchem")
    load1 = earthchem_nabu(harvest)
    load2 = earthchem_nabuprov(load1)
    load3 = earthchem_nabuorg(load2)
    load4 = earthchem_naburelease(load3)
    load5 = earthchem_uploadrelease(load4)
    report2=earthchem_missingreport_grpah(load5)
    report3=earthchem_graph_reports(report2)

