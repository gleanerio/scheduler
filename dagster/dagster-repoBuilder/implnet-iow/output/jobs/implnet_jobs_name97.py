from dagster import job

from ops.implnet_ops_name97 import harvest_name97

@job
def implnet_job_name97():
    harvest_name97()