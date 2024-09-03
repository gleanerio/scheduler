from dagster import job

from ops.implnet_ops_iow_usgs_sta__0 import harvest_iow_usgs_sta__0

@job
def implnet_job_iow_usgs_sta__0():
    harvest_iow_usgs_sta__0()
