from dagster import job

from ops.implnet_ops_ref39 import harvest_ref39

@job
def implnet_job_ref39():
    harvest_ref39()