from dagster import job

from ops.implnet_ops_links0 import harvest_links0

@job
def implnet_job_links0():
    harvest_links0()