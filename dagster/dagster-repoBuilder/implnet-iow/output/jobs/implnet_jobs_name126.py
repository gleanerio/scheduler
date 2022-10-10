from dagster import job

from ops.implnet_ops_name126 import harvest_name126

@job
def implnet_job_name126():
    harvest_name126()