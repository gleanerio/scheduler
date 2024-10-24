from dagster import job

from ..ops.implnet_ops_ecrr_examples import reload_ecrr_examples

@job
def job_ecrr_examples():
    reload_ecrr_examples()
