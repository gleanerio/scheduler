from dagster import job

from ops.implnet_ops_uva import harvest_uva

@job
def implnet_job_uva():
    harvest_uva()