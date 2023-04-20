from dagster import job

from ops.implnet_ops_huc12pp0 import harvest_huc12pp0

@job
def implnet_job_huc12pp0():
    harvest_huc12pp0()