import distutils
import time

from dagster import job, op, graph,In, Nothing, get_dagster_logger
import os, json, io
import urllib
from urllib import request
from urllib.error import HTTPError

from docker.types import RestartPolicy, ServiceMode
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
from docker.types.services import ContainerSpec, TaskTemplate, ConfigReference

DEBUG=(os.getenv('DEBUG', 'False').lower()  == 'true')
# volume and netowrk need to be the names in docker, and not the names of the object in docker compose
GLEANER_CONFIG_VOLUME=os.environ.get('GLEANERIO_CONFIG_VOLUME', "dagster_gleaner_configs")
# Vars and Envs
GLEANER_HEADLESS_NETWORK=os.environ.get('GLEANERIO_HEADLESS_NETWORK', "headless_gleanerio")
# env items
URL = os.environ.get('PORTAINER_URL')
APIKEY = os.environ.get('PORTAINER_KEY')


GLEANER_MINIO_ADDRESS = str(os.environ.get('GLEANERIO_MINIO_ADDRESS'))
GLEANER_MINIO_PORT = str(os.environ.get('GLEANERIO_MINIO_PORT'))
GLEANER_MINIO_USE_SSL = bool(distutils.util.strtobool(os.environ.get('GLEANERIO_MINIO_USE_SSL')))
GLEANER_MINIO_SECRET_KEY = str(os.environ.get('GLEANERIO_MINIO_SECRET_KEY'))
GLEANER_MINIO_ACCESS_KEY = str(os.environ.get('GLEANERIO_MINIO_ACCESS_KEY'))
GLEANER_MINIO_BUCKET =str( os.environ.get('GLEANERIO_MINIO_BUCKET'))
GLEANER_HEADLESS_ENDPOINT = str(os.environ.get('GLEANERIO_HEADLESS_ENDPOINT', "http://headless:9222"))
# using GLEANER, even though this is a nabu property... same prefix seems easier
GLEANER_GRAPH_URL = str(os.environ.get('GLEANERIO_GRAPH_URL'))
GLEANER_GRAPH_NAMESPACE = str(os.environ.get('GLEANERIO_GRAPH_NAMESPACE'))
GLEANERIO_GLEANER_CONFIG_PATH= str(os.environ.get('GLEANERIO_GLEANER_CONFIG_PATH', "/gleaner/gleanerconfig.yaml"))
GLEANERIO_NABU_CONFIG_PATH= str(os.environ.get('GLEANERIO_NABU_CONFIG_PATH', "/nabu/nabuconfig.yaml"))
GLEANERIO_GLEANER_IMAGE =str( os.environ.get('GLEANERIO_GLEANER_IMAGE', 'nsfearthcube/gleaner:latest'))
GLEANERIO_NABU_IMAGE = str(os.environ.get('GLEANERIO_NABU_IMAGE', 'nsfearthcube/nabu:latest'))
GLEANERIO_LOG_PREFIX = str(os.environ.get('GLEANERIO_LOG_PREFIX', 'scheduler/logs/')) # path to logs in nabu/gleaner
GLEANERIO_GLEANER_ARCHIVE_OBJECT = str(os.environ.get('GLEANERIO_GLEANER_ARCHIVE_OBJECT', 'scheduler/configs/GleanerCfg.tgz'))
GLEANERIO_GLEANER_ARCHIVE_PATH = str(os.environ.get('GLEANERIO_GLEANER_ARCHIVE_PATH', '/gleaner/'))
GLEANERIO_NABU_ARCHIVE_OBJECT=str(os.environ.get('GLEANERIO_NABU_ARCHIVE_OBJECT', 'scheduler/configs/NabuCfg.tgz'))
GLEANERIO_NABU_ARCHIVE_PATH=str(os.environ.get('GLEANERIO_NABU_ARCHIVE_PATH', '/nabu/'))
GLEANERIO_GLEANER_DOCKER_CONFIG=str(os.environ.get('GLEANERIO_GLEANER_DOCKER_CONFIG', 'gleaner'))
GLEANERIO_NABU_DOCKER_CONFIG=str(os.environ.get('GLEANERIO_NABU_DOCKER_CONFIG', 'nabu'))
def _graphEndpoint():
    url = f"{GLEANER_GRAPH_URL}/namespace/{GLEANER_GRAPH_NAMESPACE}/sparql"
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
    server =  _pythonMinioUrl(GLEANER_MINIO_ADDRESS) + ":" + GLEANER_MINIO_PORT
    get_dagster_logger().info(f"S3 URL    : {GLEANER_MINIO_ADDRESS}")
    get_dagster_logger().info(f"S3 PYTHON SERVER : {server}")
    get_dagster_logger().info(f"S3 PORT   : {GLEANER_MINIO_PORT}")
    # get_dagster_logger().info(f"S3 read started : {str(os.environ.get('GLEANER_MINIO_KEY'))}")
    # get_dagster_logger().info(f"S3 read started : {str(os.environ.get('GLEANER_MINIO_SECRET'))}")
    get_dagster_logger().info(f"S3 BUCKET : {GLEANER_MINIO_BUCKET}")
    get_dagster_logger().debug(f"S3 object : {str(object)}")

    client = Minio(
        server,
        # secure=True,
        secure = GLEANER_MINIO_USE_SSL,
        access_key=GLEANER_MINIO_ACCESS_KEY,
        secret_key=GLEANER_MINIO_SECRET_KEY,
    )
    try:
        data = client.get_object(GLEANER_MINIO_BUCKET, object)
        return data
    except S3Error as err:
        get_dagster_logger().info(f"S3 read error : {str(err)}")


def s3loader(data, name):
    secure= GLEANER_MINIO_USE_SSL
    if (GLEANER_MINIO_PORT and GLEANER_MINIO_PORT == "80"
             and secure == False):
        server = _pythonMinioUrl(GLEANER_MINIO_ADDRESS)
    elif (GLEANER_MINIO_PORT and GLEANER_MINIO_PORT == "443"
                and secure == True):
        server = _pythonMinioUrl(GLEANER_MINIO_ADDRESS)
    else:
        # it's not on a normal port
        server = f"{_pythonMinioUrl(GLEANER_MINIO_ADDRESS)}:{GLEANER_MINIO_PORT}"

    client = Minio(
        server,
        secure=secure,
        #secure = bool(distutils.util.strtobool(os.environ.get('GLEANER_MINIO_SSL'))),
        access_key=GLEANER_MINIO_ACCESS_KEY,
        secret_key=GLEANER_MINIO_SECRET_KEY,
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
    objPrefix = GLEANERIO_LOG_PREFIX + logname
    f = io.BytesIO()
    #length = f.write(bytes(json_str, 'utf-8'))
    length = f.write(data)
    f.seek(0)
    client.put_object(GLEANER_MINIO_BUCKET,
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

    if GLEANER_MINIO_USE_SSL:
        proto = "https"
    port = GLEANER_MINIO_PORT
    address = GLEANER_MINIO_ADDRESS
    bucket = GLEANER_MINIO_BUCKET
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
    get_dagster_logger().info(f"create docker client")
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


def _create_service(
    op_context: OpExecutionContext,
    client,
    container_context: DockerContainerContext,
    image: str,
    entrypoint: Optional[Sequence[str]],
    command: Optional[Sequence[str]],
        name="",
        workingdir="/",

):
    env_vars = dict([parse_env_var(env_var) for env_var in container_context.env_vars])
    get_dagster_logger().info(f"create docker service for {name}")
    ## thoguhts
    # return service, container, since there is one
    restart_policy  = RestartPolicy(condition='none')
    # docker.py if replicated job, total completions = replicas
    # replicas =0 you do not get a container
    serivce_mode = ServiceMode("replicated-job",concurrency=1,replicas=1)
    get_dagster_logger().info(str(client.configs.list()))
  #  gleanerid = client.configs.list(filters={"name":{"gleaner-eco": "true"}})
    gleanerconfig = client.configs.list(filters={"name": [GLEANERIO_GLEANER_DOCKER_CONFIG]})
    get_dagster_logger().info(f"docker config gleaner id {str(gleanerconfig[0].id)}")
    nabuconfig = client.configs.list(filters={"name":[GLEANERIO_NABU_DOCKER_CONFIG]})
    get_dagster_logger().info(f"docker config nabu id {str(nabuconfig[0].id)}")
    get_dagster_logger().info(f"create docker service for {name}")
    gleaner = ConfigReference(gleanerconfig[0].id, GLEANERIO_GLEANER_DOCKER_CONFIG,GLEANERIO_GLEANER_CONFIG_PATH)
    nabu = ConfigReference(nabuconfig[0].id, GLEANERIO_NABU_DOCKER_CONFIG,GLEANERIO_NABU_CONFIG_PATH)
    configs = [gleaner,nabu]
   # name = name if len(name) else _get_container_name(op_context.run_id, op_context.op.name, op_context.retry_number),
    service = client.services.create(
        image,
        args=command,
        env= env_vars,
        name=name ,
        networks= container_context.networks if len(container_context.networks) else None,
        restart_policy = restart_policy,
        mode=serivce_mode,
        workdir=workingdir,
        configs=configs
    )
    wait_count =0
    while True:
        time.sleep(1)
        wait_count+=1
        get_dagster_logger().debug(str(service.tasks()))

        container_task = service.tasks(filters={"service":name})

        containers = client.containers.list(all=True, filters={"label":f"com.docker.swarm.service.name={name}"})
        if len(containers)> 0:
            break
        if wait_count > 12:
            raise f"Container  for service {name} not starting"

    get_dagster_logger().info(len(containers))
    return service, containers[0]




def gleanerio(context, mode, source):
    ## ------------   Create
    returnCode = 0
    get_dagster_logger().info(f"Gleanerio mode: {str(mode)}")

    if str(mode) == "gleaner":
        IMAGE =GLEANERIO_GLEANER_IMAGE

       # ARGS = f"gleaner --cfg/gleaner/gleanerconfig.yaml -source {source} --rude"
        ARGS = ["--cfg", GLEANERIO_GLEANER_CONFIG_PATH,"-source", source, "--rude"]
        NAME = f"sch_{source}_{str(mode)}"
        WorkingDir = "/gleaner/"
        #Entrypoint = ["/gleaner/gleaner", "--cfg", "/gleaner/gleanerconfig.yaml", "-source", source, "--rude"]
        # LOGFILE = 'log_gleaner.txt'  # only used for local log file writing
    elif (str(mode) == "prune"):
        IMAGE = GLEANERIO_NABU_IMAGE

        ARGS = ["--cfg", GLEANERIO_NABU_CONFIG_PATH, "prune", "--prefix", "summoned/" + source]
        NAME = f"sch_{source}_{str(mode)}"
        WorkingDir = "/nabu/"
        Entrypoint = "nabu"
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
    elif (str(mode) == "prov"):
        IMAGE = GLEANERIO_NABU_IMAGE

        ARGS = ["--cfg",  GLEANERIO_NABU_CONFIG_PATH, "prefix", "--prefix", "prov/" + source]
        NAME = f"sch_{source}_{str(mode)}"
        WorkingDir = "/nabu/"
        Entrypoint = "nabu"
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
    elif (str(mode) == "orgs"):
        IMAGE = GLEANERIO_NABU_IMAGE

        ARGS = ["--cfg",  GLEANERIO_NABU_CONFIG_PATH, "prefix", "--prefix", "orgs"]
        NAME = f"sch_{source}_{str(mode)}"
        WorkingDir = "/nabu/"
        Entrypoint = "nabu"
        # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
    elif (str(mode) == "release"):
        IMAGE = GLEANERIO_NABU_IMAGE

        ARGS = ["--cfg",  GLEANERIO_NABU_CONFIG_PATH, "release", "--prefix", "summoned/" + source]
        NAME = f"sch_{source}_{str(mode)}"
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
        data["Cmd"] = ARGS
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
           # "Binds":  [f"{GLEANER_CONFIG_VOLUME}:/configs"]
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
                              # "volumes": {
                              #                             f"{GLEANER_CONFIG_VOLUME}":
                              #                                 {'bind': '/configs', 'mode': 'rw'}
                              #                             },


            },
        )
        container_context = run_container_context.merge(op_container_context)
        get_dagster_logger().info(f"call docker _get_client: ")
        client = _get_client(container_context)

        try:
            get_dagster_logger().info(f"try docker _create_service: ")
            service, container = _create_service(
                context, client, container_context, IMAGE, "", data["Cmd"], name=NAME,
                workingdir=data["WorkingDir"]
            )
        except Exception as err:
            raise err


        cid = container.id # legacy til the start get's fixed



        ## ------------  Archive to load, which is how to send in the config (from where?)




        # do not let a possible issue with container logs  stop log upload.
        ## I thinkthis happens when a container exits immediately.
        try:
            for line in container.logs(stdout=True, stderr=True, stream=True, follow=True):
                get_dagster_logger().debug(line)  # noqa: T201
        except docker.errors.APIError as ex:
            get_dagster_logger().info(f"watch container logs failed Docker API ISSUE: {repr(ex)}")
        except Exception as ex:
            get_dagster_logger().info(f"watch container logs failed other issue:{repr(ex)} ")


        # ## ------------  Wait expect 200
        # we want to get the logs, no matter what, so do not exit, yet.
        ## or should logs be moved into finally?
        ### in which case they need to be methods that don't send back errors.
        exit_status = container.wait()["StatusCode"]
        get_dagster_logger().info(f"Container Wait Exit status:  {exit_status}")
        # WE PULL THE LOGS, then will throw an error
        returnCode = exit_status




        ## ------------  Copy logs  expect 200


        c = container.logs(stdout=True, stderr=True, stream=False, follow=False).decode('latin-1')

        # write to s3

        s3loader(str(c).encode(), NAME)  # s3loader needs a bytes like object
        #s3loader(str(c).encode('utf-8'), NAME)  # s3loader needs a bytes like object
        # write to minio (would need the minio info here)

        get_dagster_logger().info(f"container Logs to s3: ")

## get log files
        url = URL + '/containers/' + cid + '/archive'
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

        if exit_status != 0:
            raise Exception(f"Gleaner/Nabu container returned exit code {exit_status}")
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
            if (service):
                service.remove()
                get_dagster_logger().info(f"Service Remove: {service.name}")
            else:
                get_dagster_logger().info(f"Service Not created, so not removed.")

        else:
            get_dagster_logger().info(f"Service {service.name} NOT Removed : DEBUG ENABLED")
        #     if (container):
        #         container.remove(force=True)
        #         get_dagster_logger().info(f"Container Remove: {container.name}")
        #     else:
        #         get_dagster_logger().info(f"Container Not created, so not removed.")
        #
        # else:
        #     get_dagster_logger().info(f"Container {container.name} NOT Removed : DEBUG ENABLED")

    if (returnCode != 0):
        get_dagster_logger().info(f"Gleaner/Nabu container non-zero exit code. See logs in S3")
        raise Exception("Gleaner/Nabu container non-zero exit code. See logs in S3")
    return returnCode

@op
def sechydrgreg0_getImage(context):
    run_container_context = DockerContainerContext.create_for_run(
        context.dagster_run,
        context.instance.run_launcher
        if isinstance(context.instance.run_launcher, DockerRunLauncher)
        else None,
    )
    get_dagster_logger().info(f"call docker _get_client: ")
    client = _get_client(run_container_context)
    client.images.pull(GLEANERIO_GLEANER_IMAGE)
    client.images.pull(GLEANERIO_NABU_IMAGE)
@op(ins={"start": In(Nothing)})
def sechydrgreg0_gleaner(context):
    returned_value = gleanerio(context, ("gleaner"), "sechydrgreg0")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"Gleaner returned  {r} ")
    return

@op(ins={"start": In(Nothing)})
def sechydrgreg0_nabu_prune(context):
    returned_value = gleanerio(context,("prune"), "sechydrgreg0")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"nabu prune returned  {r} ")
    return

@op(ins={"start": In(Nothing)})
def sechydrgreg0_nabuprov(context):
    returned_value = gleanerio(context,("prov"), "sechydrgreg0")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"nabu prov returned  {r} ")
    return

@op(ins={"start": In(Nothing)})
def sechydrgreg0_nabuorg(context):
    returned_value = gleanerio(context,("orgs"), "sechydrgreg0")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"nabu org load returned  {r} ")
    return

@op(ins={"start": In(Nothing)})
def sechydrgreg0_naburelease(context):
    returned_value = gleanerio(context,("release"), "sechydrgreg0")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"nabu release returned  {r} ")
    return
@op(ins={"start": In(Nothing)})
def sechydrgreg0_uploadrelease(context):
    returned_value = postRelease("sechydrgreg0")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"upload release returned  {r} ")
    return


@op(ins={"start": In(Nothing)})
def sechydrgreg0_missingreport_s3(context):
    source = getSitemapSourcesFromGleaner(GLEANERIO_GLEANER_CONFIG_PATH, sourcename="sechydrgreg0")
    source_url = source.get('url')
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "sechydrgreg0"
    graphendpoint = None
    milled = False
    summon = True
    returned_value = missingReport(source_url, bucket, source_name, s3Minio, graphendpoint, milled=milled, summon=summon)
    r = str('missing repoort returned value:{}'.format(returned_value))
    report = json.dumps(returned_value, indent=2)
    s3Minio.putReportFile(bucket, source_name, "missing_report_s3.json", report)
    get_dagster_logger().info(f"missing s3 report  returned  {r} ")
    return
@op(ins={"start": In(Nothing)})
def sechydrgreg0_missingreport_graph(context):
    source = getSitemapSourcesFromGleaner(GLEANERIO_GLEANER_CONFIG_PATH, sourcename="sechydrgreg0")
    source_url = source.get('url')
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "sechydrgreg0"

    graphendpoint = _graphEndpoint()# f"{os.environ.get('GLEANER_GRAPH_URL')}/namespace/{os.environ.get('GLEANER_GRAPH_NAMESPACE')}/sparql"

    milled = True
    summon = False # summon only off
    returned_value = missingReport(source_url, bucket, source_name, s3Minio, graphendpoint, milled=milled, summon=summon)
    r = str('missing report graph returned value:{}'.format(returned_value))
    report = json.dumps(returned_value, indent=2)

    s3Minio.putReportFile(bucket, source_name, "missing_report_graph.json", report)
    get_dagster_logger().info(f"missing graph  report  returned  {r} ")
    return
@op(ins={"start": In(Nothing)})
def sechydrgreg0_graph_reports(context) :
    source = getSitemapSourcesFromGleaner(GLEANERIO_GLEANER_CONFIG_PATH, sourcename="sechydrgreg0")
    #source_url = source.get('url')
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "sechydrgreg0"

    graphendpoint = _graphEndpoint() # f"{os.environ.get('GLEANER_GRAPH_URL')}/namespace/{os.environ.get('GLEANER_GRAPH_NAMESPACE')}/sparql"

    milled = False
    summon = True
    returned_value = generateGraphReportsRepo(source_name,  graphendpoint, reportList=reportTypes["repo_detailed"])
    r = str('returned value:{}'.format(returned_value))
    #report = json.dumps(returned_value, indent=2) # value already json.dumps
    report = returned_value
    s3Minio.putReportFile(bucket, source_name, "graph_stats.json", report)
    get_dagster_logger().info(f"graph report  returned  {r} ")
    return

@op(ins={"start": In(Nothing)})
def sechydrgreg0_identifier_stats(context):
    source = getSitemapSourcesFromGleaner(GLEANERIO_GLEANER_CONFIG_PATH, sourcename="sechydrgreg0")
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "sechydrgreg0"

    returned_value = generateIdentifierRepo(source_name, bucket, s3Minio)
    r = str('returned value:{}'.format(returned_value))
    #r = str('identifier stats returned value:{}'.format(returned_value))
    report = returned_value.to_json()
    s3Minio.putReportFile(bucket, source_name, "identifier_stats.json", report)
    get_dagster_logger().info(f"identifer stats report  returned  {r} ")
    return

@op(ins={"start": In(Nothing)})
def sechydrgreg0_bucket_urls(context):
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
    bucket = GLEANER_MINIO_BUCKET
    source_name = "sechydrgreg0"

    res = s3Minio.listSummonedUrls(bucket, source_name)
    r = str('returned value:{}'.format(res))
    bucketurls = json.dumps(res, indent=2)
    s3Minio.putReportFile(GLEANER_MINIO_BUCKET, source_name, "bucketutil_urls.json", bucketurls)
    get_dagster_logger().info(f"bucker urls report  returned  {r} ")
    return


#Can we simplify and use just a method. Then import these methods?
# def missingreport_s3(context, msg: str, source="sechydrgreg0"):
#
#     source= getSitemapSourcesFromGleaner(GLEANERIO_GLEANER_CONFIG_PATH, sourcename=source)
#     source_url = source.get('url')
#     s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), None)
#     bucket = GLEANER_MINIO_BUCKET
#     source_name="sechydrgreg0"
#
#     graphendpoint = None
#     milled = False
#     summon = True
#     returned_value = missingReport(source_url, bucket, source_name, s3Minio, graphendpoint, milled=milled, summon=summon)
#     r = str('returned value:{}'.format(returned_value))
#     return msg + r
@graph
def harvest_sechydrgreg0():
    containers = sechydrgreg0_getImage()
    harvest = sechydrgreg0_gleaner(start=containers)

# defingin nothing dependencies
    # https://docs.dagster.io/concepts/ops-jobs-graphs/graphs#defining-nothing-dependencies

    report_ms3 = sechydrgreg0_missingreport_s3(start=harvest)
    report_idstat = sechydrgreg0_identifier_stats(start=report_ms3)
    # for some reason, this causes a msg parameter missing
    report_bucketurl = sechydrgreg0_bucket_urls(start=report_idstat)

    #report1 = missingreport_s3(harvest, source="sechydrgreg0")
    load_release = sechydrgreg0_naburelease(start=harvest)
    load_uploadrelease = sechydrgreg0_uploadrelease(start=load_release)

    load_prune = sechydrgreg0_nabu_prune(start=load_uploadrelease)
    load_prov = sechydrgreg0_nabuprov(start=load_prune)
    load_org = sechydrgreg0_nabuorg(start=load_prov)

# run after load
    report_msgraph=sechydrgreg0_missingreport_graph(start=load_org)
    report_graph=sechydrgreg0_graph_reports(start=report_msgraph)




