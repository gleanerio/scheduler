from dagster import job

from ops.implnet_ops_invemartraining import harvest_invemartraining

@job
def implnet_job_invemartraining():
    harvest_invemartraining()