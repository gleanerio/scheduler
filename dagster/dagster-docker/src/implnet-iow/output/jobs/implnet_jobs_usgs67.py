from dagster import job

from ops.implnet_ops_usgs67 import harvest_usgs67

@job
def implnet_job_usgs67():
    harvest_usgs67()