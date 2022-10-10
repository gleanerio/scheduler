from dagster import job

from ops.implnet_ops_usgs86 import harvest_usgs86

@job
def implnet_job_usgs86():
    harvest_usgs86()