import io
import os
from typing import Any, Mapping, Optional, Sequence

#from dagster import Field
from pydantic import Field

import pydash
from dagster import ConfigurableResource, Config, EnvVar, get_dagster_logger



import time
from datetime import datetime
import requests

import docker
from docker.types import RestartPolicy, ServiceMode

from dagster import In, Nothing, OpExecutionContext, StringSource, op

from dagster._core.utils import parse_env_var


from dagster_docker.container_context import DockerContainerContext
from dagster_docker.docker_run_launcher import DockerRunLauncher
from dagster_docker.utils import DOCKER_CONFIG_SCHEMA, validate_docker_image
from docker.types.services import ContainerSpec, TaskTemplate, ConfigReference

from .graph import GraphResource,BlazegraphResource
from .gleanerS3 import gleanerS3Resource

#Let's try to use dasgeter aws as the minio configuration

#
# # Vars and Envs
# GLEANER_HEADLESS_NETWORK=os.environ.get('GLEANERIO_HEADLESS_NETWORK', "headless_gleanerio")
# # env items
# URL = os.environ.get('PORTAINER_URL')
# APIKEY = os.environ.get('PORTAINER_KEY')
# CONTAINER_WAIT_TIMEOUT= os.environ.get('GLEANERIO_CONTAINER_WAIT_SECONDS', 5)
#
# Let's try to use dasgeter aws as the minio configuration
# GLEANER_MINIO_ADDRESS = str(os.environ.get('GLEANERIO_MINIO_ADDRESS'))
# GLEANER_MINIO_PORT = str(os.environ.get('GLEANERIO_MINIO_PORT'))
# GLEANER_MINIO_USE_SSL = bool(distutils.util.strtobool(os.environ.get('GLEANERIO_MINIO_USE_SSL')))
# GLEANER_MINIO_SECRET_KEY = str(os.environ.get('GLEANERIO_MINIO_SECRET_KEY'))
# GLEANER_MINIO_ACCESS_KEY = str(os.environ.get('GLEANERIO_MINIO_ACCESS_KEY'))
# GLEANER_MINIO_BUCKET =str( os.environ.get('GLEANERIO_MINIO_BUCKET'))
#
# # set for the earhtcube utiltiies
# MINIO_OPTIONS={"secure":GLEANER_MINIO_USE_SSL
#
#               ,"access_key": GLEANER_MINIO_ACCESS_KEY
#               ,"secret_key": GLEANER_MINIO_SECRET_KEY
#                }
#
# GLEANER_HEADLESS_ENDPOINT = str(os.environ.get('GLEANERIO_HEADLESS_ENDPOINT', "http://headless:9222"))
# # using GLEANER, even though this is a nabu property... same prefix seems easier
# GLEANER_GRAPH_URL = str(os.environ.get('GLEANERIO_GRAPH_URL'))
# GLEANER_GRAPH_NAMESPACE = str(os.environ.get('GLEANERIO_GRAPH_NAMESPACE'))
# GLEANERIO_GLEANER_CONFIG_PATH= str(os.environ.get('GLEANERIO_GLEANER_CONFIG_PATH', "/gleaner/gleanerconfig.yaml"))
# GLEANERIO_NABU_CONFIG_PATH= str(os.environ.get('GLEANERIO_NABU_CONFIG_PATH', "/nabu/nabuconfig.yaml"))
# GLEANERIO_GLEANER_IMAGE =str( os.environ.get('GLEANERIO_GLEANER_IMAGE', 'nsfearthcube/gleaner:latest'))
# GLEANERIO_NABU_IMAGE = str(os.environ.get('GLEANERIO_NABU_IMAGE', 'nsfearthcube/nabu:latest'))
# GLEANERIO_LOG_PREFIX = str(os.environ.get('GLEANERIO_LOG_PREFIX', 'scheduler/logs/')) # path to logs in nabu/gleaner
# GLEANERIO_GLEANER_ARCHIVE_OBJECT = str(os.environ.get('GLEANERIO_GLEANER_ARCHIVE_OBJECT', 'scheduler/configs/GleanerCfg.tgz'))
# GLEANERIO_GLEANER_ARCHIVE_PATH = str(os.environ.get('GLEANERIO_GLEANER_ARCHIVE_PATH', '/gleaner/'))
# GLEANERIO_NABU_ARCHIVE_OBJECT=str(os.environ.get('GLEANERIO_NABU_ARCHIVE_OBJECT', 'scheduler/configs/NabuCfg.tgz'))
# GLEANERIO_NABU_ARCHIVE_PATH=str(os.environ.get('GLEANERIO_NABU_ARCHIVE_PATH', '/nabu/'))
# GLEANERIO_GLEANER_DOCKER_CONFIG=str(os.environ.get('GLEANERIO_GLEANER_DOCKER_CONFIG', 'gleaner'))
# GLEANERIO_NABU_DOCKER_CONFIG=str(os.environ.get('GLEANERIO_NABU_DOCKER_CONFIG', 'nabu'))
# #GLEANERIO_SUMMARY_GRAPH_ENDPOINT = os.environ.get('GLEANERIO_SUMMARY_GRAPH_ENDPOINT')
# GLEANERIO_SUMMARY_GRAPH_NAMESPACE = os.environ.get('GLEANERIO_SUMMARY_GRAPH_NAMESPACE',f"{GLEANER_GRAPH_NAMESPACE}_summary" )
#
# SUMMARY_PATH = 'graphs/summary'
# RELEASE_PATH = 'graphs/latest'

# this will probably need to handle the client, and the
class GleanerioResource(ConfigurableResource):

    DEBUG_CONTAINER: bool
    # docker/portainer API
    GLEANERIO_DOCKER_URL: str =  Field(
         description="Docker Endpoint URL.")
    GLEANERIO_PORTAINER_APIKEY: str =  Field(
         description="Portainer API Key.")
    # Dokcerhub container images
    GLEANERIO_GLEANER_IMAGE: str = Field(
        description="GLEANERIO_GLEANER_IMAGE.")
    GLEANERIO_NABU_IMAGE: str = Field(
        description="GLEANERIO_NABU_IMAGE.")

    # docker swarm resources. Presently a network and config names
    GLEANERIO_DOCKER_HEADLESS_NETWORK: str = Field(
        description="GLEANERIO_HEADLESS_NETWORK.")
    GLEANERIO_DOCKER_GLEANER_CONFIG: str = Field(
        description="GLEANERIO_DOCKER_GLEANER_CONFIG.")
    GLEANERIO_DOCKER_NABU_CONFIG: str = Field(
        description="GLEANERIO_DOCKER_NABU_CONFIG.")

    GLEANERIO_HEADLESS_ENDPOINT:str = Field(
        description="GLEANERIO_HEADLESS_NETWORK.", default="http://headless:9000/")

# location where config file will be mounted in container
    GLEANERIO_GLEANER_CONFIG_PATH: str = Field(
        description="GLEANERIO_DOCKER_GLEANER_CONFIG_PATH.")

    GLEANERIO_NABU_CONFIG_PATH: str = Field(
        description="GLEANERIO_DOCKER_NABU_CONFIG_PATH.")

# Execution parameter. The logs from LOG_PREFIX will be uploaded to s3 every n seconds.
    GLEANERIO_DOCKER_CONTAINER_WAIT_TIMEOUT: int = Field(
        description="CONTAINER_WAIT_TIMEOUT.", default=600)
    GLEANERIO_LOG_PREFIX: str = Field(
        description="GLEANERIO_DOCKER_LOG_PREFIX.")

    GLEANERIO_DAGSTER_CONFIG_PATH: str = Field(
        description="DAGSTER_GLEANERIO_CONFIG_PATH for Project.")
    gs3: gleanerS3Resource   # this will be a botocore.client.S3.
    triplestore: GraphResource  # should be a blazegraph... but let's try generic
    GLEANERIO_GRAPH_NAMESPACE:str = Field(
        description="GLEANERIO_GRAPH_NAMESPACE for Project.")
    GLEANERIO_GRAPH_SUMMARY_NAMESPACE:str = Field(
        description="GLEANERIO_GRAPH_SUMMARY_NAMESPACE for Project.")

    # at present, these are hard coded as os.getenv in sensors.gleaner_summon.sources_schedule
    GLEANERIO_SCHEDULE_DEFAULT :str = Field(
        description="GLEANERIO_SCHEDULE_DEFAULT for Project.", default="@weekly")
    GLEANERIO_SCHEDULE_DEFAULT_TIMEZONE :str = Field(
        description="GLEANERIO_SCHEDULE_DEFAULT_TIMEZONE for Project.", default="America/Los_Angeles")

    def _get_client(self, docker_container_context: DockerContainerContext):
        headers = {'X-API-Key': self.GLEANERIO_PORTAINER_APIKEY}
        client = docker.DockerClient(base_url=self.GLEANERIO_DOCKER_URL, version="1.47")
        # client = docker.APIClient(base_url=URL, version="1.35")
        get_dagster_logger().info(f"create docker client")
        if (client.api._general_configs):
            client.api._general_configs["HttpHeaders"] = headers
        else:
            client.api._general_configs = {"HttpHeaders": headers}
        client.api.headers['X-API-Key'] =  self.GLEANERIO_PORTAINER_APIKEY
        get_dagster_logger().info(f" docker version {client.version()}")
        if docker_container_context.registry:
            client.login(
                registry=docker_container_context.registry["url"],
                username=docker_container_context.registry["username"],
                password=docker_container_context.registry["password"],
            )
        return client

    def _create_service(self,
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
        restart_policy = RestartPolicy(condition='none')
        # docker.py if replicated job, total completions = replicas
        # replicas =0 you do not get a container
        serivce_mode = ServiceMode("replicated-job", concurrency=1, replicas=1)
        get_dagster_logger().info(str(client.configs.list()))
        #  gleanerid = client.configs.list(filters={"name":{"gleaner-eco": "true"}})
        gleanerconfig = client.configs.list(filters={"name": [self.GLEANERIO_DOCKER_GLEANER_CONFIG]})
        if gleanerconfig is not None and len(gleanerconfig ) >0:
            get_dagster_logger().info(f"docker config gleaner id {str(gleanerconfig[0].id)}")
        else:
            raise Exception(f"docker config '{self.GLEANERIO_DOCKER_GLEANER_CONFIG}' not found. Please add Gleaner/Nabu configuration files to docker.")
        nabuconfig = client.configs.list(filters={"name": [self.GLEANERIO_DOCKER_NABU_CONFIG]})
        if nabuconfig is not None and len(nabuconfig) >0 :
            get_dagster_logger().info(f"docker config nabu id {str(nabuconfig[0].id)}")
        else:
            raise Exception(f"docker config '{self.GLEANERIO_DOCKER_NABU_CONFIG}' not found. Please add Gleaner/Nabu configuration files to docker.")
        get_dagster_logger().info(f"create docker service for {name}")
        gleaner = ConfigReference(gleanerconfig[0].id, self.GLEANERIO_DOCKER_GLEANER_CONFIG, self.GLEANERIO_GLEANER_CONFIG_PATH)
        nabu = ConfigReference(nabuconfig[0].id, self.GLEANERIO_DOCKER_NABU_CONFIG, self.GLEANERIO_NABU_CONFIG_PATH)
        configs = [gleaner, nabu]
        # name = name if len(name) else _get_container_name(op_context.run_id, op_context.op.name, op_context.retry_number),
        service = client.services.create(
            image,
            args=command,
            env=env_vars,
            name=name,
            networks=container_context.networks if len(container_context.networks) else None,
            restart_policy=restart_policy,
            mode=serivce_mode,
            workdir=workingdir,
            configs=configs
        )
        wait_count = 0
        while True:
            time.sleep(1)
            wait_count += 1
            get_dagster_logger().debug(str(service.tasks()))

            container_task = service.tasks(filters={"service": name})

            containers = client.containers.list(all=True, filters={"label": f"com.docker.swarm.service.name={name}"})
            if len(containers) > 0:
                break
            if wait_count > 12:
                raise f"Container  for service {name} not starting"

        get_dagster_logger().info(len(containers))
        return service, containers[0]

    def getImage(self,context):
        run_container_context = DockerContainerContext.create_for_run(
            context.dagster_run,
            context.instance.run_launcher
            if isinstance(context.instance.run_launcher, DockerRunLauncher)
            else None,
        )
        get_dagster_logger().info(f"call docker _get_client: ")
        client = self.get_client(run_container_context)
        client.images.pull(self.GLEANERIO_GLEANER_IMAGE)
        client.images.pull(self.GLEANERIO_NABU_IMAGE)

    def s3loader(self,data, name, date_string=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")):
        logname = name + '_{}.log'.format(date_string)
        objPrefix = self.GLEANERIO_LOG_PREFIX + logname
        f = io.BytesIO()
        # length = f.write(bytes(json_str, 'utf-8'))
        length = f.write(data)
        f.seek(0)
        self.gs3.s3.get_client().put_object(Bucket=self.gs3.GLEANERIO_MINIO_BUCKET,
                          Key=objPrefix,
                          Body=f,  # io.BytesIO(data),
                          ContentLength=length,  # len(data),
                          ContentType="text/plain"
                          )
        get_dagster_logger().info(f"Log uploaded: {str(objPrefix)}")
# rewrite so that we pass in the image, args, name working dir.
    # we want to setup 'sensors' for when assets are returned by these
    # data -> returns summon directory, and a release file.

    def execute(self,context, mode, source):
        ## ------------   Create
        returnCode = 0
        get_dagster_logger().info(f"Gleanerio mode: {str(mode)}")
        date_string = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        if str(mode) == "gleaner":
            IMAGE =self.GLEANERIO_GLEANER_IMAGE

           # ARGS = f"gleaner --cfg/gleaner/gleanerconfig.yaml -source {source} --rude"
            ARGS = ["--cfg", self.GLEANERIO_GLEANER_CONFIG_PATH,"-source", source, "--rude"]
            NAME = f"sch_{source}_{str(mode)}"
            WorkingDir = "/gleaner/"
            #Entrypoint = ["/gleaner/gleaner", "--cfg", "/gleaner/gleanerconfig.yaml", "-source", source, "--rude"]
            # LOGFILE = 'log_gleaner.txt'  # only used for local log file writing
        elif (str(mode) == "prune"):
            IMAGE = self.GLEANERIO_NABU_IMAGE

            ARGS = ["--cfg", self.GLEANERIO_NABU_CONFIG_PATH, "prune", "--prefix", "summoned/" + source]
            NAME = f"sch_{source}_{str(mode)}"
            WorkingDir = "/nabu/"
            Entrypoint = "nabu"
            # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
        elif (str(mode) == "prov"):
            IMAGE = self.GLEANERIO_NABU_IMAGE

            ARGS = ["--cfg",  self.GLEANERIO_NABU_CONFIG_PATH, "prefix", "--prefix", "prov/" + source]
            NAME = f"sch_{source}_{str(mode)}"
            WorkingDir = "/nabu/"
            Entrypoint = "nabu"
            # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
        elif (str(mode) == "orgs"):
            IMAGE = self.GLEANERIO_NABU_IMAGE

            ARGS = ["--cfg",  self.GLEANERIO_NABU_CONFIG_PATH, "prefix", "--prefix", "orgs"]
            NAME = f"sch_{source}_{str(mode)}"
            WorkingDir = "/nabu/"
            Entrypoint = "nabu"
            # LOGFILE = 'log_nabu.txt'  # only used for local log file writing
        elif (str(mode) == "release"):
            IMAGE = self.GLEANERIO_NABU_IMAGE

            ARGS = ["--cfg",  self.GLEANERIO_NABU_CONFIG_PATH, "release", "--prefix", "summoned/" + source]
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
            enva.append(str("MINIO_ADDRESS={}".format(self.gs3.GLEANERIO_MINIO_ADDRESS))) # the python needs to be wrapped, this does not
            enva.append(str("MINIO_PORT={}".format(self.gs3.GLEANERIO_MINIO_PORT)))
            #enva.append(str("MINIO_USE_SSL={}".format(self.gs3.GLEANER_MINIO_USE_SSL)))
            enva.append(str("MINIO_USE_SSL={}".format(self.gs3.s3.use_ssl)))
            #enva.append(str("MINIO_SECRET_KEY={}".format(self.gs3.GLEANER_MINIO_SECRET_KEY)))
            #enva.append(str("MINIO_ACCESS_KEY={}".format(self.gs3.GLEANER_MINIO_ACCESS_KEY)))
            enva.append(str("MINIO_SECRET_KEY={}".format(self.gs3.s3.aws_secret_access_key)))
            enva.append(str("MINIO_ACCESS_KEY={}".format(self.gs3.s3.aws_access_key_id)))
            #enva.append(str("MINIO_BUCKET={}".format(self.gs3.GLEANER_MINIO_BUCKET)))
            enva.append(str("MINIO_BUCKET={}".format(self.gs3.GLEANERIO_MINIO_BUCKET)))
            enva.append(str("SPARQL_ENDPOINT={}".format(self.triplestore.GraphEndpoint(self.GLEANERIO_GRAPH_NAMESPACE))))
            enva.append(str("GLEANER_HEADLESS_ENDPOINT={}".format(self.GLEANERIO_HEADLESS_ENDPOINT)))
            enva.append(str("GLEANERIO_DOCKER_HEADLESS_NETWORK={}".format(self.GLEANERIO_DOCKER_HEADLESS_NETWORK)))

            data["Env"] = enva
            data["HostConfig"] = {
                "NetworkMode": self.GLEANERIO_DOCKER_HEADLESS_NETWORK,
            }


    # docker dagster
            get_dagster_logger().info(f"start docker code region: ")


            # trying to get headers in:
            # https://github.com/docker/docker-py/blob/84414e343e526cf93f285284dd2c2c40f703e4a9/docker/utils/decorators.py#L45
            op_container_context = DockerContainerContext(
                # registry=registry,
                env_vars=enva,
                networks=[self.GLEANERIO_DOCKER_HEADLESS_NETWORK],
                container_kwargs={"working_dir": data["WorkingDir"],
                                  # "volumes": {
                                  #                             f"{GLEANER_CONFIG_VOLUME}":
                                  #                                 {'bind': '/configs', 'mode': 'rw'}
                                  #                             },


                },
            )
            container_context = run_container_context.merge(op_container_context)
            get_dagster_logger().info(f"call docker _get_client: ")
            client = self._get_client(container_context)

            try:
                get_dagster_logger().info(f"try docker _create_service: ")
                service, container = self._create_service(
                    context, client, container_context, IMAGE, "", data["Cmd"], name=NAME,
                    workingdir=data["WorkingDir"]
                )
            except Exception as err:
                raise err


            cid = container.id # legacy til the start get's fixed


    # Removed watching the logs, in favor of periodic upload
            wait_count = 0
            while True:
                wait_count += 1
                try:
                    container.wait(timeout=self.GLEANERIO_DOCKER_CONTAINER_WAIT_TIMEOUT)
                    exit_status = container.wait()["StatusCode"]
                    get_dagster_logger().info(f"Container Wait Exit status:  {exit_status}")
                    # WE PULL THE LOGS, then will throw an error
                    returnCode = exit_status
                    c = container.logs(stdout=True, stderr=True, stream=False, follow=False).decode('latin-1')

                    # write to s3
  # use minio_resource

                    self.s3loader(str(c).encode(), NAME, date_string=date_string)  # s3loader needs a bytes like object

                    # s3loader(str(c).encode('utf-8'), NAME)  # s3loader needs a bytes like object
                    # write to minio (would need the minio info here)

                    get_dagster_logger().info(f"container Logs to s3: ")
    # this needs to be address at some point. https://www.appsloveworld.com/docker/100/85/docker-py-getarchive-destination-folder
                    path = f"{WorkingDir}/logs"
                    tar_archive_stream, tar_stat = container.get_archive(path)
                    archive = bytearray()
                    for chunk in tar_archive_stream:
                        archive.extend(chunk)
                    # use minio_resource
                    self.s3loader(archive, f"{source}_{mode}_runlogs", date_string=date_string)
                    get_dagster_logger().info(f"uploaded logs : {source}_{mode}_runlogs to  {path}")
                    break
                except requests.exceptions.ReadTimeout as ex:
                    path = f"{WorkingDir}/logs"
                    tar_archive_stream, tar_stat = container.get_archive(path)
                    archive = bytearray()
                    for chunk in tar_archive_stream:
                        archive.extend(chunk)
                    # use minio_resource
                    self.s3loader(archive, f"{source}_{mode}_runlogs", date_string=date_string)
                    get_dagster_logger().info(f"uploaded {wait_count}th log : {source}_{mode}_runlogs to  {path}")
                except docker.errors.APIError as ex:
                    get_dagster_logger().info(f"Container Wait docker API error :  {str(ex)}")
                    returnCode = 1
                    break
                if container.status == 'exited' or container.status == 'removed':
                    get_dagster_logger().info(f"Container exited or removed. status:  {container.status}")
                    exit_status = container.wait()["StatusCode"]
                    returnCode = exit_status
                    # use minio_resource
                    self.s3loader(str(c).encode(), NAME)  # s3loader needs a bytes like object
                    # s3loader(str(c).encode('utf-8'), NAME)  # s3loader needs a bytes like object
                    # write to minio (would need the minio info here)

                    get_dagster_logger().info(f"container Logs to s3: ")
                    # this needs to be address at some point. https://www.appsloveworld.com/docker/100/85/docker-py-getarchive-destination-folder
                    path = f"{WorkingDir}/logs"
                    tar_archive_stream, tar_stat = container.get_archive(path)
                    archive = bytearray()
                    for chunk in tar_archive_stream:
                        archive.extend(chunk)
                    # use minio_resource
                    self.s3loader(archive, f"{source}_{mode}_runlogs", date_string=date_string)
                    get_dagster_logger().info(f"uploaded logs : {source}_{mode}_runlogs to  {path}")
                    break

        # ABOVE Future, need to extraxct files, and upload
        # pw_tar = tarfile.TarFile(fileobj=StringIO(d.decode('utf-8')))
        #    pw_tar.extractall("extract_to/")


            if exit_status != 0:
                raise Exception(f"Gleaner/Nabu container returned exit code {exit_status}")
        finally:
            if (not self.DEBUG_CONTAINER) :
                if (service):
                    service.remove()
                    get_dagster_logger().info(f"Service Remove: {service.name}")
                else:
                    get_dagster_logger().info(f"Service Not created, so not removed.")

            else:
                get_dagster_logger().info(f"Service {service.name} NOT Removed : DEBUG ENABLED")


        if (returnCode != 0):
            get_dagster_logger().info(f"Gleaner/Nabu container non-zero exit code. See logs in S3")
            raise Exception("Gleaner/Nabu container non-zero exit code. See logs in S3")
        return returnCode
