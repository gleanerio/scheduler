from dagster import job

from ops.implnet_ops_abacus import harvest_abacus

@job
def implnet_job_abacus():
    harvest_abacus()