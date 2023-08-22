from dagster import job

from ops.implnet_ops_ecrr_examples import harvest_ecrr_examples

@job
def implnet_job_ecrr_examples():
    harvest_ecrr_examples()