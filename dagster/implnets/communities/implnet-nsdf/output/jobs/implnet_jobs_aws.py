from dagster import job

from ops.implnet_ops_aws import harvest_aws

@job
def implnet_job_aws():
    harvest_aws()