import os, json, io
import urllib
from urllib import request
from dagster import job, op, get_dagster_logger
from minio import Minio
from minio.error import S3Error
from datetime import datetime

# Usage:  dagit -h host -f file.py

# @op
# def get_file_sizes():
#     files = [f for f in os.listdir(".") if os.path.isfile(f)]
#     for f in files:
#         get_dagster_logger().info(f"Size of {f} is {os.path.getsize(f)}")

# for the template, only the SOURCEVAL needs to set in the CMD env.
# maybe for the logfile too?

## TODOs
# - the log file name is static in the point where the log is loaded to s3

CMD = ["--cfg", "/gleaner/testGleanerCfg.yaml", "--source", "edmo"]
NAME = "gleaner01"
LOGFILE = 'log_gleaner.txt'  #  only used for local log file writing

# CMD = ["--cfg", "/nabu/testNabuCfg.yaml", "prefix", "summoned/edmo"]
# NAME = "nabu01"
# LOGFILE = 'log_nabu.txt'   #  only used for local log file writing

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

## ------------  defs

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

@op
def apitest():
    req = request.Request(URL + 'containers/json', method="GET")
    req.add_header('X-API-Key', APIKEY)
    r = request.urlopen(req)
    c = r.read()
    d = json.loads(c)
    print(d[0]['Names'])
    get_dagster_logger().info(f"Name(s): {str((d[3]['Names']))}")


@op
def gleanerioflow_op():
    ## ------------   Create

    data = {}
    data["Image"] = IMAGE
    data["Cmd"] = CMD

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
    r = request.urlopen(req)
    c = r.read()
    d = json.loads(c)
    cid = d['Id']

    print(r.status)
    get_dagster_logger().info(f"Create: {str(r.status)}")

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
    DATA = s3reader()

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
    c = r.read()

    # write to file
    # f = open(LOGFILE, 'w')
    # f.write(str(c))
    # f.close()

    # write to s3
    s3loader(str(c).encode()) # s3loader needs a bytes like object

    # write to minio (would need the minio info here)

    get_dagster_logger().info(f"Logs: {str(r.status)}")

    ## ------------  Remove   expect 204

    url = URL + 'containers/' + cid
    req = request.Request(url, method="DELETE")
    req.add_header('X-API-Key', APIKEY)
    # req.add_header('content-type', 'application/json')
    req.add_header('accept', 'application/json')
    r = request.urlopen(req)
    print(r.status)
    get_dagster_logger().info(f"Remove: {str(r.status)}")


@job
def nabu_job():
    gleanerioflow_op()
