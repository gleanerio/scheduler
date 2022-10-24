from dagster import job

from ops.implnet_ops_bco-dmo import harvest_bco-dmo

@job
def implnet_job_bco-dmo():
    harvest_bco-dmo()