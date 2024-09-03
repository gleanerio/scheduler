from dagster import job

from ops.implnet_ops_usgs_hydrologicunit__0 import harvest_usgs_hydrologicunit__0

@job
def implnet_job_usgs_hydrologicunit__0():
    harvest_usgs_hydrologicunit__0()
