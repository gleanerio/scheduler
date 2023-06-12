from dagster import job

from ops.implnet_ops_geocodes_demo_datasets import harvest_geocodes_demo_datasets

@job
def implnet_job_geocodes_demo_datasets():
    harvest_geocodes_demo_datasets()