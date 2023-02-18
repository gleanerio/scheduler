from dagster import job

from ops.implnet_ops_invemarexperts import harvest_invemarexperts

@job
def implnet_job_invemarexperts():
    harvest_invemarexperts()