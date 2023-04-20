from dagster import job

from ops.implnet_ops_pesquisa import harvest_pesquisa

@job
def implnet_job_pesquisa():
    harvest_pesquisa()