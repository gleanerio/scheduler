from dagster import job

from ops.implnet_ops_asulrdr import harvest_asulrdr

@job
def implnet_job_asulrdr():
    harvest_asulrdr()