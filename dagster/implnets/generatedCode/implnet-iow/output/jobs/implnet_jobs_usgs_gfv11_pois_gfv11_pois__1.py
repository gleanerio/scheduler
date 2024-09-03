from dagster import job

from ops.implnet_ops_usgs_gfv11_pois_gfv11_pois__1 import harvest_usgs_gfv11_pois_gfv11_pois__1

@job
def implnet_job_usgs_gfv11_pois_gfv11_pois__1():
    harvest_usgs_gfv11_pois_gfv11_pois__1()
