from dagster import job

from ops.implnet_ops_invemarinstitutions import harvest_invemarinstitutions

@job
def implnet_job_invemarinstitutions():
    harvest_invemarinstitutions()