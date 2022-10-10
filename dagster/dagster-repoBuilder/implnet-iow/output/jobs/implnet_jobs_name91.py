from dagster import job

from ops.implnet_ops_name91 import harvest_name91

@job
def implnet_job_name91():
    harvest_name91()