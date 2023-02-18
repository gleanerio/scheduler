from dagster import job

from ops.implnet_ops_hydrologicunit0 import harvest_hydrologicunit0

@job
def implnet_job_hydrologicunit0():
    harvest_hydrologicunit0()