from dagster import job

from ops.implnet_ops_oceanscape import harvest_oceanscape

@job
def implnet_job_oceanscape():
    harvest_oceanscape()