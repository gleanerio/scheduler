from dagster import job

from ops.implnet_ops_invemarinstitution import harvest_invemarinstitution

@job
def implnet_job_invemarinstitution():
    harvest_invemarinstitution()