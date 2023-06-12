from dagster import job

from ops.implnet_ops_cifor import harvest_cifor

@job
def implnet_job_cifor():
    harvest_cifor()