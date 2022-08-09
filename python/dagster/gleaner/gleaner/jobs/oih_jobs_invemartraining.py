from dagster import job

from gleaner.ops.oih_invemartraining import harvest_invemartraining

@job
def oih_job_invemartraining():
    harvest_invemartraining()