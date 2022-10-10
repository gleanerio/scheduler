from dagster import job

from ops.implnet_ops_name163 import harvest_name163

@job
def implnet_job_name163():
    harvest_name163()