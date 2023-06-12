from dagster import job

from ops.implnet_ops_ofd import harvest_ofd

@job
def implnet_job_ofd():
    harvest_ofd()