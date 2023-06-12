from dagster import job

from ops.implnet_ops_neotomadb import harvest_neotomadb

@job
def implnet_job_neotomadb():
    harvest_neotomadb()