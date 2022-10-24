from dagster import job

from ops.implnet_ops_usap-dc import harvest_usap-dc

@job
def implnet_job_usap-dc():
    harvest_usap-dc()