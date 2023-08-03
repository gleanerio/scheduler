import distutils

from dagster import job, op, graph, get_dagster_logger
import os, json, io
import urllib
from urllib import request
from urllib.error import HTTPError
from dagster import job, op, get_dagster_logger
from ec.gleanerio.gleaner import getGleaner, getSitemapSourcesFromGleaner
import json

from minio import Minio
from minio.error import S3Error
from datetime import datetime
from ec.reporting.report import missingReport, generateGraphReportsRepo, reportTypes, generateIdentifierRepo
from ec.datastore import s3
import requests
import logging as log
from urllib.error import HTTPError

from typing import Any, Mapping, Optional, Sequence

import docker
from dagster import Field, In, Nothing, OpExecutionContext, StringSource, op
from dagster._annotations import experimental
from dagster._core.utils import parse_env_var
from dagster._serdes.utils import hash_str

from dagster_docker.container_context import DockerContainerContext
from dagster_docker.docker_run_launcher import DockerRunLauncher
from dagster_docker.utils import DOCKER_CONFIG_SCHEMA, validate_docker_image

DEBUG=(os.getenv('DEBUG', 'False').lower()  == 'true')
# volume and netowrk need to be the names in docker, and not the names of the object in docker compose
GLEANER_CONFIG_VOLUME=os.environ.get('GLEANER_CONFIG_VOLUME', "dagster_gleaner_configs")
# Vars and Envs
GLEANER_HEADLESS_NETWORK=os.environ.get('GLEANER_HEADLESS_NETWORK', "headless_gleanerio")
# env items
URL = os.environ.get('PORTAINER_URL')
APIKEY = os.environ.get('PORTAINER_KEY')


GLEANER_MINIO_ADDRESS = os.environ.get('GLEANER_MINIO_ADDRESS')
GLEANER_MINIO_PORT = os.environ.get('GLEANER_MINIO_PORT')
GLEANER_MINIO_USE_SSL = os.environ.get('GLEANER_MINIO_USE_SSL')
GLEANER_MINIO_SECRET_KEY = os.environ.get('GLEANER_MINIO_SECRET_KEY')
GLEANER_MINIO_ACCESS_KEY = os.environ.get('GLEANER_MINIO_ACCESS_KEY')
GLEANER_MINIO_BUCKET = os.environ.get('GLEANER_MINIO_BUCKET')
GLEANER_HEADLESS_ENDPOINT = os.environ.get('GLEANER_HEADLESS_ENDPOINT', "http://headless:9222")
# using GLEANER, even though this is a nabu property... same prefix seems easier
GLEANER_GRAPH_URL = os.environ.get('GLEANER_GRAPH_URL')
GLEANER_GRAPH_NAMESPACE = os.environ.get('GLEANER_GRAPH_NAMESPACE')
GLEANERIO_GLEANER_CONFIG_PATH= os.environ.get('GLEANERIO_GLEANER_CONFIG_PATH', "/gleaner/gleanerconfig.yaml")
GLEANERIO_NABU_CONFIG_PATH= os.environ.get('GLEANERIO_NABU_CONFIG_PATH', "/nabu/nabuconfig.yaml")

def _graphEndpoint():
    url = f"{os.environ.get('GLEANER_GRAPH_URL')}/namespace/{os.environ.get('GLEANER_GRAPH_NAMESPACE')}/sparql"
    return url

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
    url = f"{_graphEndpoint()}?uri={release_url}" # f"{os.environ.get('GLEANER_GRAPH_URL')}/namespace/{os.environ.get('GLEANER_GRAPH_NAMESPACE')}/sparql?uri={release_url}"
    get_dagster_logger().info(f'graph: insert "{source}" to {url} ')
    r = requests.post(url)
    log.debug(f' status:{r.status_code}')  # status:404
    get_dagster_logger().info(f'graph: insert: status:{r.status_code}')
    if r.status_code == 200:
        # '<?xml version="1.0"?><data modified="0" milliseconds="7"/>'
        if 'data modified="0"' in r.text:
            get_dagster_logger().info(f'graph: no data inserted ')
            raise Exception("No Data Added: " + r.text)
        return True
    else:
        get_dagster_logger().info(f'graph: error')
        raise Exception(f' graph: insert failed: status:{r.status_code}')

def _get_client(docker_container_context: DockerContainerContext):
    headers = {'X-API-Key': APIKEY}
    client = docker.DockerClient(base_url=URL, version="1.43" )
    #client = docker.APIClient(base_url=URL, version="1.35")
    get_dagster_logger().info(f"creat docker client")
    if (client.api._general_configs):
        client.api._general_configs["HttpHeaders"] = headers
    else:
        client.api._general_configs={"HttpHeaders":headers}
    client.api.headers['X-API-Key'] = APIKEY
    get_dagster_logger().info(f" docker version {client.version()}")
    if docker_container_context.registry:
        client.login(
            registry=docker_container_context.registry["url"],
            username=docker_container_context.registry["username"],
            password=docker_container_context.registry["password"],
        )
    return client


def _get_container_name(run_id, op_name, retry_number):
    container_name = hash_str(run_id + op_name)

    retry_number = retry_number
    if retry_number > 0:
        container_name = f"{container_name}-{retry_number}"

    return container_name


def _create_container(
    op_context: OpExecutionContext,
    client,
    container_context: DockerContainerContext,
    image: str,
    entrypoint: Optional[Sequence[str]],
    command: Optional[Sequence[str]],
        name=""
):
    env_vars = dict([parse_env_var(env_var) for env_var in container_context.env_vars])
    get_dagster_logger().info(f"creat docker container")
    return client.containers.create(
        image,
        name=name if len(name) else _get_container_name(op_context.run_id, op_context.op.name, op_context.retry_number),
        detach=True,
        network=container_context.networks[0] if len(container_context.networks) else None,
  #      entrypoint=entrypoint,
        command=command,
        environment=env_vars,
        **container_context.container_kwargs,
    )

def gleanerio(context, mode, source):
    ## ------------   Create
    returnCode = 0
    get_dagster_logger().info(f"Gleanerio mode: {str(mode)}")

    if str(mode) == "gleaner":
        IMAGE = os.environ.get('GLEANERIO_GLEANER_IMAGE')
        ARCHIVE_FILE = os.environ.get('GLEANERIO_GLEANER_ARCHIVE_OBJECT')
        ARCHIVE_PATH = os.environ.get('GLEANERIO_GLEANER_ARCHIVE_PATH')
       # CMD = f"gleaner --cfg/gleaner/gleanerconfig.yaml -source {source} --rude"
        CMD = ["--cfg", GLEANERIO_GLEANER_CONFIG_PATH,"-source", source, "--rude"]
        NAME = f"gleaner01_{source}_{str(mode)}"
        WorkingDir = "/gleaner/"
        #Entrypoint = ["/gleaner/gleaner", "--cfg", "/gleaner/gleanerconfig.yaml", "-source", source, "--rude"]
        # LOGFILE = 'log_gleaner.txt'  # only used for local log file writing
    elif (str(mode) == "nabu"):
        IMAGE = os.environ.get('GLEANERIO_NABU_IMAGE')
        ARCHIVE_FILE = os.environ.get('GLEANERIO_NABU_ARCHIVE_OBJECT')
        ARCHIVE_PATH = os.environ.get('GLEANERIO_NABU_ARCHIVE_PATH')
        CMD = ["--cfg", GLEANERIO_NABU_CONFIG_PATH, "prune", "--prefix", "summoned/" + source]
        NAME = f"nabu01_{source}_{str(mode)}"
        WorkingDir = "/nabu/"
        Entrypoint = "nabu"
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
    elif (str(mode) == "prov"):
        IMAGE = os.environ.get('GLEANERIO_NABU_IMAGE')
        ARCHIVE_FILE = os.environ.get('GLEANERIO_NABU_ARCHIVE_OBJECT')
        ARCHIVE_PATH = os.environ.get('GLEANERIO_NABU_ARCHIVE_PATH')
        CMD = ["--cfg",  GLEANERIO_NABU_CONFIG_PATH, "prefix", "--prefix", "prov/" + source]
        NAME = f"nabu01_{source}_{str(mode)}"
        WorkingDir = "/nabu/"
        Entrypoint = "nabu"
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
    elif (str(mode) == "orgs"):
        IMAGE = os.environ.get('GLEANERIO_NABU_IMAGE')
        ARCHIVE_FILE = os.environ.get('GLEANERIO_NABU_ARCHIVE_OBJECT')
        ARCHIVE_PATH = os.environ.get('GLEANERIO_NABU_ARCHIVE_PATH')
        CMD = ["--cfg",  GLEANERIO_NABU_CONFIG_PATH, "prefix", "--prefix", "orgs"]
        NAME = f"nabu01_{source}_{str(mode)}"
        WorkingDir = "/nabu/"
        Entrypoint = "nabu"
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
    elif (str(mode) == "release"):
        IMAGE = os.environ.get('GLEANERIO_NABU_IMAGE')
        ARCHIVE_FILE = os.environ.get('GLEANERIO_NABU_ARCHIVE_OBJECT')
        ARCHIVE_PATH = os.environ.get('GLEANERIO_NABU_ARCHIVE_PATH')
        CMD = ["--cfg",  GLEANERIO_NABU_CONFIG_PATH, "release", "--prefix", "summoned/" + source]
        NAME = f"nabu01_{source}_{str(mode)}"
        WorkingDir = "/nabu/"
        Entrypoint = "nabu"
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
    else:

        returnCode = 1
        return returnCode

    # from docker0dagster
    run_container_context = DockerContainerContext.create_for_run(
        context.dagster_run,
        context.instance.run_launcher
        if isinstance(context.instance.run_launcher, DockerRunLauncher)
        else None,
    )
    validate_docker_image(IMAGE)

    try:
        # setup data/body for  container create
        data = {}
        data["Image"] = IMAGE
        data["WorkingDir"] = WorkingDir
        #data["Entrypoint"] = Entrypoint
        data["Cmd"] = CMD
#### gleaner
        # v.BindEnv("minio.address", "MINIO_ADDRESS")
        # v.BindEnv("minio.port", "MINIO_PORT")
        # v.BindEnv("minio.ssl", "MINIO_USE_SSL")
        # v.BindEnv("minio.accesskey", "MINIO_ACCESS_KEY")
        # v.BindEnv("minio.secretkey", "MINIO_SECRET_KEY")
        # v.BindEnv("minio.bucket", "MINIO_BUCKET")
        # // v.BindEnv("minio.region", "MINIO_REGION")
        # v.BindEnv("sparql.endpoint", "SPARQL_ENDPOINT")
        # v.BindEnv("sparql.authenticate", "SPARQL_AUTHENTICATE")
        # v.BindEnv("sparql.username", "SPARQL_USERNAME")
        # v.BindEnv("sparql.password", "SPARQL_PASSWORD")
        # v.BindEnv("s3.domain", "S3_DOMAIN")
### gleaner summoner config
        # viperSubtree.BindEnv("headless", "GLEANER_HEADLESS_ENDPOINT")
        # viperSubtree.BindEnv("threads", "GLEANER_THREADS")
        # viperSubtree.BindEnv("mode", "GLEANER_MODE")

        #### NABU config
        # minioSubtress.BindEnv("address", "MINIO_ADDRESS")
        # minioSubtress.BindEnv("port", "MINIO_PORT")
        # minioSubtress.BindEnv("ssl", "MINIO_USE_SSL")
        # minioSubtress.BindEnv("accesskey", "MINIO_ACCESS_KEY")
        # minioSubtress.BindEnv("secretkey", "MINIO_SECRET_KEY")
        # minioSubtress.BindEnv("secretkey", "MINIO_SECRET_KEY")
        # minioSubtress.BindEnv("bucket", "MINIO_BUCKET")
        # viperSubtree.BindEnv("endpoint", "SPARQL_ENDPOINT")
        ###### nabu sparql config
        # viperSubtree.BindEnv("endpointBulk", "SPARQL_ENDPOINTBULK")
        # viperSubtree.BindEnv("endpointMethod", "SPARQL_ENDPOINTMETHOD")
        # viperSubtree.BindEnv("contentType", "SPARQL_CONTENTTYPE")
        # viperSubtree.BindEnv("authenticate", "SPARQL_AUTHENTICATE")
        # viperSubtree.BindEnv("username", "SPARQL_USERNAME")
        # viperSubtree.BindEnv("password", "SPARQL_PASSWORD")
        ### NABU object
        # viperSubtree.BindEnv("bucket", "MINIO_BUCKET")
        # viperSubtree.BindEnv("domain", "S3_DOMAIN")
        # add in env variables here"Env": ["FOO=bar","BAZ=quux"],

        # TODO: Build SPARQL_ENDPOINT from  GLEANER_GRAPH_URL, GLEANER_GRAPH_NAMESPACE
        enva = []
        enva.append(str("MINIO_ADDRESS={}".format(GLEANER_MINIO_ADDRESS)))
        enva.append(str("MINIO_PORT={}".format(GLEANER_MINIO_PORT)))
        enva.append(str("MINIO_USE_SSL={}".format(GLEANER_MINIO_USE_SSL)))
        enva.append(str("MINIO_SECRET_KEY={}".format(GLEANER_MINIO_SECRET_KEY)))
        enva.append(str("MINIO_ACCESS_KEY={}".format(GLEANER_MINIO_ACCESS_KEY)))
        enva.append(str("MINIO_BUCKET={}".format(GLEANER_MINIO_BUCKET)))
        enva.append(str("SPARQL_ENDPOINT={}".format(_graphEndpoint())))
        enva.append(str("GLEANER_HEADLESS_ENDPOINT={}".format(GLEANER_HEADLESS_ENDPOINT)))
        enva.append(str("GLEANER_HEADLESS_NETWORK={}".format(GLEANER_HEADLESS_NETWORK)))

        data["Env"] = enva
        data["HostConfig"] = {
            "NetworkMode": GLEANER_HEADLESS_NETWORK,
            "Binds":  [f"{GLEANER_CONFIG_VOLUME}:/configs"]
        }
        # data["Volumes"] = [
        #     "dagster-project:/configs"
        # ]
        # we would like this to be "dagster-${PROJECT:-eco}" but that is a bit tricky
        # end setup of data

# docker dagster
        get_dagster_logger().info(f"start docker code region: ")
        # trying to get headers in:
        # https://github.com/docker/docker-py/blob/84414e343e526cf93f285284dd2c2c40f703e4a9/docker/utils/decorators.py#L45
        op_container_context = DockerContainerContext(
            # registry=registry,
            env_vars=enva,
            networks=[GLEANER_HEADLESS_NETWORK],
            container_kwargs={"working_dir": data["WorkingDir"],
                              "volumes": {
                                                          f"{GLEANER_CONFIG_VOLUME}":
                                                              {'bind': '/configs', 'mode': 'rw'}
                                                          },


            },
        )
        container_context = run_container_context.merge(op_container_context)
        get_dagster_logger().info(f"call docker _get_client: ")
        client = _get_client(container_context)

        try:
            get_dagster_logger().info(f"try docker _create_container: ")
            container = _create_container(
                context, client, container_context, IMAGE, "", data["Cmd"], name=NAME
            )
        except docker.errors.ImageNotFound:
            client.images.pull(IMAGE)
            container = _create_container(
                context, client, container_context, IMAGE, "", data["Cmd"], name=NAME
            )

        if len(container_context.networks) > 1:
            for network_name in container_context.networks[1:]:
                network = client.networks.get(network_name)
                network.connect(container)

        cid = container.id # legacy til the start get's fixed



        ## ------------  Archive to load, which is how to send in the config (from where?)


        DATA = s3reader(ARCHIVE_FILE)
        container.put_archive(ARCHIVE_PATH,DATA )


        ## ------------  Start
        ## note new issue:
        # {"message": "starting container with non-empty request body was deprecated since API v1.22 and removed in v1.24"}
        EMPTY_DATA="{}".encode('utf-8')
        url = URL + 'containers/' + cid + '/start'
        get_dagster_logger().info(f"Container start url: {url}")
        req = request.Request(url,data=EMPTY_DATA, method="POST")
        req.add_header('X-API-Key', APIKEY)
        req.add_header('content-type', 'application/json')
        req.add_header('accept', 'application/json')
        try:
            r = request.urlopen(req)
        except HTTPError as err:
            get_dagster_logger().fatal(f"Container Start failed: {str(err.code)} reason: {err.reason}")
            raise err
        except Exception as err:
            print("failed to start container:  unknown reason: ", err)
            get_dagster_logger().info(f"Create Failed: unknown reason {str(err)}")
            raise err
        print(r.status)
        get_dagster_logger().info(f"Start container: {str(r.status)}")

        # container.start()
        # client.api.start(container=container.id)
        ## start is not working
        try:
            for line in container.logs(stdout=True, stderr=True, stream=True, follow=True):
                get_dagster_logger().debug(line)  # noqa: T201
        except docker.errors.APIError as ex:
            get_dagster_logger().info(f"watch container logs failed Docker API ISSUE: ", ex)
            returnCode = 1
        except Exception as ex:
            get_dagster_logger().info(f"watch container logs failed other issue: ", ex)
            returnCode = 1

        # ## ------------  Wait expect 200
        # we want to get the logs, no matter what, so do not exit, yet.
        ## or should logs be moved into finally?
        ### in which case they need to be methods that don't send back errors.
        exit_status = container.wait()["StatusCode"]
        get_dagster_logger().info(f"Container Wait Exit status:  {exit_status}")
        returnCode = exit_status




        ## ------------  Copy logs  expect 200


        c = container.logs(stdout=True, stderr=True, stream=False, follow=False).decode('latin-1')

        # write to s3

        s3loader(str(c).encode(), NAME)  # s3loader needs a bytes like object
        #s3loader(str(c).encode('utf-8'), NAME)  # s3loader needs a bytes like object
        # write to minio (would need the minio info here)

        get_dagster_logger().info(f"container Logs to s3: {str(r.status)}")

## get log files
        url = URL + 'containers/' + cid + '/archive'
        params = {
            'path': f"{WorkingDir}/logs"
        }
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        # print(url)
        req = request.Request(url, method="GET")
        req.add_header('X-API-Key', APIKEY)
        req.add_header('content-type', 'application/x-compressed')
        req.add_header('accept', 'application/json')
        r = request.urlopen(req)

        log.info(f"{r.status} ")
        get_dagster_logger().info(f"Container Archive Retrieved: {str(r.status)}")
        # s3loader(r.read().decode('latin-1'), NAME)
        s3loader(r.read(), f"{source}_{mode}_runlogs")
    # Future, need to extraxct files, and upload
    # pw_tar = tarfile.TarFile(fileobj=StringIO(d.decode('utf-8')))
    #    pw_tar.extractall("extract_to/")

    # looks like get_archive also has issues. Returns nothing,
       #  strm, stat =  container.get_archive(f"{WorkingDir}/logs/")
       #  get_dagster_logger().info(f"container Logs to s3: {str(stat)}")
       #
       #  i =0
       #  for d in strm:
       #      r = d.decode('utf-8')
       # # s3loader(r.read().decode('latin-1'), NAME)
       #      s3loader(r.encode(), f"{source}_{i}_runlogs")
       #      i+=1

       # s3loader(r.read().decode('latin-1'), NAME)

    finally:
        if (not DEBUG) :
            # if (cid):
            #     url = URL + 'containers/' + cid
            #     req = request.Request(url, method="DELETE")
            #     req.add_header('X-API-Key', APIKEY)
            #     # req.add_header('content-type', 'application/json')
            #     req.add_header('accept', 'application/json')
            #     r = request.urlopen(req)
            #     print(r.status)
            #     get_dagster_logger().info(f"Container Remove: {str(r.status)}")
            # else:
            #     get_dagster_logger().info(f"Container Not created, so not removed.")
            if (container):
                container.remove(force=True)
                get_dagster_logger().info(f"Container Remove: {str(r.status)}")
            else:
                get_dagster_logger().info(f"Container Not created, so not removed.")
        else:
            get_dagster_logger().info(f"Container NOT Remove: DEBUG ENABLED")

    if (returnCode != 0):
        get_dagster_logger().info(f"Gleaner/Nabu container non-zero exit code. See logs in S3")
        raise Exception("Gleaner/Nabu container non-zero exit code. See logs in S3")
    return returnCode

@op
def bcodmo_gleaner(context)-> str:
    returned_value = gleanerio(context, ("gleaner"), "bcodmo")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"Gleaner notes are  {r} ")
    return r

@op
def bcodmo_nabu_prune(context, msg: str)-> str:
    returned_value = gleanerio(context,("nabu"), "bcodmo")
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def bcodmo_nabuprov(context, msg: str)-> str:
    returned_value = gleanerio(context,("prov"), "bcodmo")
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def bcodmo_nabuorg(context, msg: str)-> str:
    returned_value = gleanerio(context,("orgs"), "bcodmo")
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def bcodmo_naburelease(context, msg: str) -> str:
    returned_value = gleanerio(context,("release"), "bcodmo")
    r = str('returned value:{}'.format(returned_value))
    return msg + r
@op
def bcodmo_uploadrelease(context, msg: str) -> str:
    returned_value = postRelease("bcodmo")
    r = str('returned value:{}'.format(returned_value))
    return msg + r


@op
def bcodmo_missingreport_s3(context, msg: str) -> str:
    source = getSitemapSourcesFromGleaner("/scheduler/gleanerconfig.yaml", sourcename="bcodmo")
    source_url = source.get('url')
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "bcodmo"
    graphendpoint = None
    milled = False
    summon = True
    returned_value = missingReport(source_url, bucket, source_name, s3Minio, graphendpoint, milled=milled, summon=summon)
    r = str('missing repoort returned value:{}'.format(returned_value))
    report = json.dumps(returned_value, indent=2)
    s3Minio.putReportFile(bucket, source_name, "missing_report_s3.json", report)
    return msg + r
@op
def bcodmo_missingreport_graph(context, msg: str) -> str:
    source = getSitemapSourcesFromGleaner("/scheduler/gleanerconfig.yaml", sourcename="bcodmo")
    source_url = source.get('url')
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "bcodmo"

    graphendpoint = _graphEndpoint()# f"{os.environ.get('GLEANER_GRAPH_URL')}/namespace/{os.environ.get('GLEANER_GRAPH_NAMESPACE')}/sparql"

    milled = True
    summon = False # summon only off
    returned_value = missingReport(source_url, bucket, source_name, s3Minio, graphendpoint, milled=milled, summon=summon)
    r = str('missing report graph returned value:{}'.format(returned_value))
    report = json.dumps(returned_value, indent=2)

    s3Minio.putReportFile(bucket, source_name, "missing_report_graph.json", report)

    return msg + r
@op
def bcodmo_graph_reports(context, msg: str) -> str:
    source = getSitemapSourcesFromGleaner("/scheduler/gleanerconfig.yaml", sourcename="bcodmo")
    #source_url = source.get('url')
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "bcodmo"

    graphendpoint = _graphEndpoint() # f"{os.environ.get('GLEANER_GRAPH_URL')}/namespace/{os.environ.get('GLEANER_GRAPH_NAMESPACE')}/sparql"

    milled = False
    summon = True
    returned_value = generateGraphReportsRepo(source_name,  graphendpoint, reportList=reportTypes["repo_detailed"])
    r = str('returned value:{}'.format(returned_value))
    #report = json.dumps(returned_value, indent=2) # value already json.dumps
    report = returned_value
    s3Minio.putReportFile(bucket, source_name, "graph_stats.json", report)

    return msg + r

@op
def bcodmo_identifier_stats(context, msg: str) -> str:
    source = getSitemapSourcesFromGleaner("/scheduler/gleanerconfig.yaml", sourcename="bcodmo")
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "bcodmo"

    returned_value = generateIdentifierRepo(source_name, bucket, s3Minio)
    r = str('returned value:{}'.format(returned_value))
    #r = str('identifier stats returned value:{}'.format(returned_value))
    report = returned_value.to_json()
    s3Minio.putReportFile(bucket, source_name, "identifier_stats.json", report)
    return msg + r

@op()
def bcodmo_bucket_urls(context, msg: str) -> str:
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "bcodmo"

    res = s3Minio.listSummonedUrls(bucket, source_name)
    r = str('returned value:{}'.format(res))
    bucketurls = json.dumps(res, indent=2)
    s3Minio.putReportFile(GLEANER_MINIO_BUCKET, source_name, "bucketutil_urls.json", bucketurls)
    return msg + r


#Can we simplify and use just a method. Then import these methods?
# def missingreport_s3(context, msg: str, source="bcodmo"):
#
#     source= getSitemapSourcesFromGleaner("/scheduler/gleanerconfig.yaml", sourcename=source)
#     source_url = source.get('url')
#     s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
#     bucket = GLEANER_MINIO_BUCKET
#     source_name="bcodmo"
#
#     graphendpoint = None
#     milled = False
#     summon = True
#     returned_value = missingReport(source_url, bucket, source_name, s3Minio, graphendpoint, milled=milled, summon=summon)
#     r = str('returned value:{}'.format(returned_value))
#     return msg + r
@graph
def harvest_bcodmo():
    harvest = bcodmo_gleaner()

    report_ms3 = bcodmo_missingreport_s3(harvest)
    report_idstat = bcodmo_identifier_stats(report_ms3)
    # for some reason, this causes a msg parameter missing
    report_bucketurl = bcodmo_bucket_urls(report_idstat)

    #report1 = missingreport_s3(harvest, source="bcodmo")
    load_release = bcodmo_naburelease(harvest)
    load_uploadrelease = bcodmo_uploadrelease(load_release)

    load_prune = bcodmo_nabu_prune(load_uploadrelease)
    load_prov = bcodmo_nabuprov(load_prune)
    load_org = bcodmo_nabuorg(load_prov)

# run after load
    report_msgraph=bcodmo_missingreport_graph(load_org)
    report_graph=bcodmo_graph_reports(report_msgraph)




