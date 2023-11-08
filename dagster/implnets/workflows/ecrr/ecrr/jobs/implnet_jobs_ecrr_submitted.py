from dagster import job

from ..ops.implnet_ops_ecrr_submitted import reload_ecrr_submitted

@job
def job_ecrr_submitted():
    reload_ecrr_submitted()
