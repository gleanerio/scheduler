from dagster import job

from ops.implnet_ops_linkedearth import harvest_linkedearth

@job
def implnet_job_linkedearth():
    harvest_linkedearth()