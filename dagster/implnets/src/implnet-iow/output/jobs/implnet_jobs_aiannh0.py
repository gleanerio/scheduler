from dagster import job

from ops.implnet_ops_aiannh0 import harvest_aiannh0

@job
def implnet_job_aiannh0():
    harvest_aiannh0()