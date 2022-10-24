from dagster import job

from ops.implnet_ops_nhdplusv231 import harvest_nhdplusv231

@job
def implnet_job_nhdplusv231():
    harvest_nhdplusv231()