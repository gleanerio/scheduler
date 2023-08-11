from dagster import job

from ops.implnet_ops_datadiscoverystudio import harvest_datadiscoverystudio

@job
def implnet_job_datadiscoverystudio():
    harvest_datadiscoverystudio()