from dagster import job

from ops.implnet_ops_hu060 import harvest_hu060

@job
def implnet_job_hu060():
    harvest_hu060()