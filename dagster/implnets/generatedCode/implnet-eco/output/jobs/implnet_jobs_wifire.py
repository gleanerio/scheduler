from dagster import job

from ops.implnet_ops_wifire import harvest_wifire

@job
def implnet_job_wifire():
    harvest_wifire()