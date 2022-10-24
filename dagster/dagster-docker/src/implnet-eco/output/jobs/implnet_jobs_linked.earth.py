from dagster import job

from ops.implnet_ops_linked.earth import harvest_linked.earth

@job
def implnet_job_linked.earth():
    harvest_linked.earth()