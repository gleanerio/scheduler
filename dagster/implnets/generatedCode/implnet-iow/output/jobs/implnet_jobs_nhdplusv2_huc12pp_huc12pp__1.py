from dagster import job

from ops.implnet_ops_nhdplusv2_huc12pp_huc12pp__1 import harvest_nhdplusv2_huc12pp_huc12pp__1

@job
def implnet_job_nhdplusv2_huc12pp_huc12pp__1():
    harvest_nhdplusv2_huc12pp_huc12pp__1()
