from dagster import job

from ops.implnet_ops_unc import harvest_unc

@job
def implnet_job_unc():
    harvest_unc()