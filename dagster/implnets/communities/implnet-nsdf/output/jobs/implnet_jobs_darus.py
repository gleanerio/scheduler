from dagster import job

from ops.implnet_ops_darus import harvest_darus

@job
def implnet_job_darus():
    harvest_darus()