from dagster import job

from gleaner.ops.implnet_invemarinstitution import harvest_invemarinstitution

@job
def implnet_job_invemarinstitution():
    harvest_invemarinstitution()