from dagster import job

from ops.implnet_ops_irs import harvest_irs

@job
def implnet_job_irs():
    harvest_irs()