import os

from dagster import Definitions, load_assets_from_modules, EnvVar
#from dagster_slack import SlackResource, make_slack_on_run_failure_sensor
from . import assets
from .sch import weekly_sch
from .assets.tennants import community_sensor

from .resources.graph import BlazegraphResource, GraphResource
from .resources.gleanerS3 import gleanerS3Resource
def _awsEndpointAddress(url, port=None, use_ssl=True):
    if use_ssl:
        protocol = "https"
    else:
        protocol = "http"
    if port is not None:
        return  f"{protocol}://{url}:{port}"
    else:
        return  f"{protocol}://{url}"

all_assets = load_assets_from_modules([assets])
weekly_data_schedule=[ weekly_sch.loadstats_schedule, weekly_sch.all_graph_stats_schedule]
minio=gleanerS3Resource(
    # GLEANER_MINIO_BUCKET =EnvVar('GLEANER_MINIO_BUCKET'),
    # GLEANER_MINIO_ADDRESS=EnvVar('GLEANER_MINIO_ADDRESS'),
    # GLEANER_MINIO_PORT=EnvVar('GLEANER_MINIO_PORT'),
    GLEANERIO_MINIO_BUCKET=EnvVar('GLEANERIO_MINIO_BUCKET'),
    GLEANERIO_MINIO_ADDRESS=EnvVar('GLEANERIO_MINIO_ADDRESS'),
    GLEANERIO_MINIO_PORT=EnvVar('GLEANERIO_MINIO_PORT'),
    GLEANERIO_MINIO_ACCESS_KEY=EnvVar('GLEANERIO_MINIO_ACCESS_KEY'),
    GLEANERIO_MINIO_SECRET_KEY=EnvVar('GLEANERIO_MINIO_SECRET_KEY'),
    endpoint_url =_awsEndpointAddress(EnvVar('GLEANERIO_MINIO_ADDRESS').get_value(), port=EnvVar('GLEANERIO_MINIO_PORT').get_value()),
    aws_access_key_id=EnvVar('GLEANERIO_MINIO_ACCESS_KEY'),
    aws_secret_access_key=EnvVar('GLEANERIO_MINIO_SECRET_KEY')
)
triplestore=BlazegraphResource(
            GLEANERIO_GRAPH_URL=EnvVar('GLEANERIO_GRAPH_URL'),
              s3=minio,
        )


resources = {
    "local": {

        "s3":minio,
        "triplestore": triplestore,
 #       "slack": SlackResource(token=EnvVar("SLACK_TOKEN")),
    },
    "production": {

        "s3":minio,
        "triplestore":triplestore,
 #       "slack":SlackResource(token=EnvVar("SLACK_TOKEN")),
    },
}

deployment_name = os.environ.get("DAGSTER_DEPLOYMENT", "local")

defs = Definitions(
    assets=all_assets,
    schedules=weekly_data_schedule,
     resources=resources[deployment_name],
    sensors=[community_sensor]
)
