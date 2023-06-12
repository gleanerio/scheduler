from dagster import job

from ops.implnet_ops_earthchem import harvest_earthchem

@job
def implnet_job_earthchem():
    harvest_earthchem()