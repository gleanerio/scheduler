from dagster import job

from ops.implnet_ops_epa30 import harvest_epa30

@job
def implnet_job_epa30():
    harvest_epa30()