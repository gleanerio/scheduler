import os, json
import urllib
from urllib import request
from dagster import job, op, get_dagster_logger

#  dagit -h ghost.lan -f test1.py

# @op
# def get_file_sizes():
#     files = [f for f in os.listdir(".") if os.path.isfile(f)]
#     for f in files:
#         get_dagster_logger().info(f"Size of {f} is {os.path.getsize(f)}")
#

URL = os.environ.get('PORTAINER_URL')
APIKEY = os.environ.get('PORTAINER_KEY')
IMAGE = 'fils/nabu:2.0.4-developement'
NAME = "nabu01"
CMD = ["--cfg", "/nabu/testNabuCfg.yaml",  "prefix", "summoned/edmo"]
ARCHIVE_FILE = "/home/fils/src/Projects/gleaner.io/scheduler/secret/APItesting/archives/testNabuCfg.tgz"
ARCHIVE_PATH = '/nabu/'
LOGFILE = 'log_nabu.txt'

## ------------  defs

def read_file_bytestream(image_path):
    data = open(image_path, 'rb').read()
    return data


@op
def apitest():
    req = request.Request(URL+'containers/json', method="GET")
    req.add_header('X-API-Key', APIKEY)
    r = request.urlopen(req)
    c = r.read()
    d = json.loads(c)
    print(d[0]['Names'])
    get_dagster_logger().info(f"Name(s): {str((d[3]['Names']))}")

@op
def nabuflow():
    ## ------------   Create

    data = {}
    data["Image"] = IMAGE
    data["Cmd"] = CMD

    url = URL+'containers/create'
    params = {
        "name": NAME
    }
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    req = request.Request(url, str.encode(json.dumps(data)))
    req.add_header('X-API-Key', APIKEY)
    req.add_header('content-type', 'application/json')
    req.add_header('accept', 'application/json')
    r = request.urlopen(req)
    c = r.read()
    d = json.loads(c)
    cid =d['Id']

    print(r.status)
    get_dagster_logger().info(f"Create: {str(r.status)}")

    # print(cid)

    ## ------------  Archive to load, which is how to send in the config (from where?)

    url = URL+'containers/'+cid+'/archive'
    params = {
        'path': ARCHIVE_PATH
    }
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    # print(url)

    DATA = read_file_bytestream(ARCHIVE_FILE)

    req = request.Request(url, data=DATA,  method="PUT")
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

    url = URL+'containers/'+cid+'/start'
    req = request.Request(url,  method="POST")
    req.add_header('X-API-Key', APIKEY)
    req.add_header('content-type', 'application/json')
    req.add_header('accept', 'application/json')
    r = request.urlopen(req)
    print(r.status)
    get_dagster_logger().info(f"Start: {str(r.status)}")


    ## ------------  Wait expect 200

    url = URL+'containers/'+cid+'/wait'
    req = request.Request(url,  method="POST")
    req.add_header('X-API-Key', APIKEY)
    req.add_header('content-type', 'application/json')
    req.add_header('accept', 'application/json')
    r = request.urlopen(req)
    print(r.status)
    get_dagster_logger().info(f"Wait: {str(r.status)}")


    ## ------------  Copy logs  expect 200

    url = URL+'containers/'+cid+'/logs'
    params = {
        'stdout': 'true',
        'stderr': 'false'
    }
    query_string = urllib.parse.urlencode(params)

    url = url + "?" + query_string
    req = request.Request(url,  method="GET")
    req.add_header('X-API-Key', APIKEY)
    req.add_header('accept', 'application/json')
    r = request.urlopen(req)
    print(r.status)
    c = r.read()

    f = open(LOGFILE, 'w')
    f.write(str(c))
    f.close()

    get_dagster_logger().info(f"Logs: {str(r.status)}")

    ## ------------  Remove   expect 204

    url = URL+'containers/'+cid
    req = request.Request(url,  method="DELETE")
    req.add_header('X-API-Key', APIKEY)
    # req.add_header('content-type', 'application/json')
    req.add_header('accept', 'application/json')
    r = request.urlopen(req)
    print(r.status)
    get_dagster_logger().info(f"Remove: {str(r.status)}")


@job
def file_sizes_job():
    nabuflow()

