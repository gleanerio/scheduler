from dagster import job

from ops.implnet_ops_geocodes_examples import harvest_geocodes_examples

@job
def implnet_job_geocodes_examples():
    harvest_geocodes_examples()