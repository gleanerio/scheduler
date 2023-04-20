from dagster import job

from ops.implnet_ops_cyvers import harvest_cyvers

@job
def implnet_job_cyvers():
    harvest_cyvers()