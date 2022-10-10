from dagster import job

from ops.implnet_ops_name151 import harvest_name151

@job
def implnet_job_name151():
    harvest_name151()