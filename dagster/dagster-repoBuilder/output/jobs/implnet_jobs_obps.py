from dagster import job

from ops.implnet_ops_obps import harvest_obps

@job
def implnet_job_obps():
    harvest_obps()