from dagster import job

from gleaner.ops.implnet_invemartraining import harvest_invemartraining

@job
def implnet_job_invemartraining():
    harvest_invemartraining()