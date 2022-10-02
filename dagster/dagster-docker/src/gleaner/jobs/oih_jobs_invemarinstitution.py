from dagster import job

from gleaner.ops.oih_invemarinstitution import harvest_invemarinstitution

@job
def oih_job_invemarinstitution():
    harvest_invemarinstitution()