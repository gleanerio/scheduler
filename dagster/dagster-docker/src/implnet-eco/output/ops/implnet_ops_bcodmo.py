from dagster import op, graph, get_dagster_logger
import subprocess
import os, json, io
import urllib
from urllib import request
from dagster import job, op, get_dagster_logger
from minio import Minio
from minio.error import S3Error
from datetime import datetime

# Vars and Envs

# env items
URL = os.environ.get('PORTAINER_URL')
APIKEY = os.environ.get('PORTAINER_KEY')

MINIO_URL = os.environ.get('GLEANER_MINIO_URL')
MINIO_PORT = os.environ.get('GLEANER_MINIO_PORT')
MINIO_SSL = os.environ.get('GLEANER_MINIO_SSL')
MINIO_SECRET = os.environ.get('GLEANER_MINIO_SECRET')
MINIO_KEY = os.environ.get('GLEANER_MINIO_KEY')
MINIO_BUCKET = os.environ.get('GLEANER_MINIO_BUCKET')


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
    server = os.environ.get('GLEANER_MINIO_URL') + ":" + os.environ.get('GLEANER_MINIO_PORT')
    bucket = str(os.environ.get('GLEANER_MINIO_BUCKET'))

    get_dagster_logger().info(f"server: : {str(server)}")
    get_dagster_logger().info(f"bucket: : {bucket}")
    get_dagster_logger().info(f"object: : {str(object)}")

    client = Minio(
        server,
        # secure=False,
        access_key=os.environ.get('GLEANER_MINIO_KEY'),
        secret_key=os.environ.get('GLEANER_MINIO_SECRET'),
    )
    try:
        data = client.get_object(bucket, object)
        return data
    except S3Error as err:
        get_dagster_logger().info(f"S3 read error : {str(err)}")


def s3loader(data, name):
    server = os.environ.get('GLEANER_MINIO_URL') + ":" + os.environ.get('GLEANER_MINIO_PORT')
    client = Minio(
        server,
        # secure=False,
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

    logname = name + '_{}.log'.format(date_string)
    objPrefix = os.environ.get('GLEANERIO_LOG_PREFIX') + logname
    client.put_object(os.environ.get('GLEANER_MINIO_BUCKET'),
                      objPrefix,
                      io.BytesIO(data),
                      len(data))
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
        CMD = ["--cfg", "/nabu/nabuconfig.yaml", "prefix",  "--prefix", "summoned/" + source]
        NAME = "nabu01_" + source
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing

    else:
        return 1

    data = {}
    data["Image"] = IMAGE
    data["Cmd"] = CMD

    # add in env variables here"Env": ["FOO=bar","BAZ=quux"],
    enva = []
    enva.append(str("MINIO_URL={}".format(MINIO_URL)))
    enva.append(str("MINIO_PORT={}".format(MINIO_PORT)))
    enva.append(str("MINIO_SSL={}".format(MINIO_SSL)))
    enva.append(str("MINIO_SECRET={}".format(MINIO_SECRET)))
    enva.append(str("MINIO_KEY={}".format(MINIO_KEY)))
    enva.append(str("MINIO_BUCKET={}".format(MINIO_BUCKET)))

    data["Env"] = enva

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
    c = r.read()

    # write to file
    # f = open(LOGFILE, 'w')
    # f.write(str(c))
    # f.close()

    # write to s3
    s3loader(str(c).encode(), NAME)  # s3loader needs a bytes like object

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

    return 0

@op
def bcodmo_gleaner():
    returned_value = gleanerio(("gleaner"), "bcodmo")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"Gleaner notes are  {r} ")
    return r

@op
def bcodmo_nabu(context, msg: str):
    returned_value = gleanerio(("nabu"), "bcodmo")
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_bcodmo():
    harvest = bcodmo_gleaner()
    load1 = bcodmo_nabu(harvest)
    # load2 = bcodmo_prov(load1)
