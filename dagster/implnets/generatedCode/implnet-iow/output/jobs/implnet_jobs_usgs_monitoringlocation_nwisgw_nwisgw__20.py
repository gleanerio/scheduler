from dagster import job

from ops.implnet_ops_usgs_monitoringlocation_nwisgw_nwisgw__20 import harvest_usgs_monitoringlocation_nwisgw_nwisgw__20

@job
def implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__20():
    harvest_usgs_monitoringlocation_nwisgw_nwisgw__20()
