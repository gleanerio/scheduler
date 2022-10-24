from dagster import job

from ops.implnet_ops_c4rsois import harvest_c4rsois

@job
def implnet_job_c4rsois():
    harvest_c4rsois()