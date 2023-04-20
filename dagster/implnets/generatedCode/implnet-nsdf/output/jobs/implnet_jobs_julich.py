from dagster import job

from ops.implnet_ops_julich import harvest_julich

@job
def implnet_job_julich():
    harvest_julich()