from dagster import job

from ops.implnet_ops_states0 import harvest_states0

@job
def implnet_job_states0():
    harvest_states0()