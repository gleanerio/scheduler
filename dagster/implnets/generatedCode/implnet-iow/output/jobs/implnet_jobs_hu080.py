from dagster import job

from ops.implnet_ops_hu080 import harvest_hu080

@job
def implnet_job_hu080():
    harvest_hu080()