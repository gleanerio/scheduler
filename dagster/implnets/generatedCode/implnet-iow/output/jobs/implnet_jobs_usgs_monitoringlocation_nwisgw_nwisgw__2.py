from dagster import job

from ops.implnet_ops_usgs_monitoringlocation_nwisgw_nwisgw__2 import harvest_usgs_monitoringlocation_nwisgw_nwisgw__2

@job
def implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__2():
    harvest_usgs_monitoringlocation_nwisgw_nwisgw__2()
