from dagster import job

from ops.implnet_ops_ifsttar import harvest_ifsttar

@job
def implnet_job_ifsttar():
    harvest_ifsttar()