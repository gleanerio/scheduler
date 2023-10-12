from dagster import job

from ops.implnet_ops_ecrr_submitted import harvest_ecrr_submitted

@job
def implnet_job_ecrr_submitted():
    harvest_ecrr_submitted()