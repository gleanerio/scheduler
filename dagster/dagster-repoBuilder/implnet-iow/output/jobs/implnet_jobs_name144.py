from dagster import job

from ops.implnet_ops_name144 import harvest_name144

@job
def implnet_job_name144():
    harvest_name144()