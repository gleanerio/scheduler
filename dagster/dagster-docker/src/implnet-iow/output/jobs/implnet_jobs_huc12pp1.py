from dagster import job

from ops.implnet_ops_huc12pp1 import harvest_huc12pp1

@job
def implnet_job_huc12pp1():
    harvest_huc12pp1()