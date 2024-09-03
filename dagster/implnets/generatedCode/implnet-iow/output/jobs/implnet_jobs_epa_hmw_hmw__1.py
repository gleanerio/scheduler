from dagster import job

from ops.implnet_ops_epa_hmw_hmw__1 import harvest_epa_hmw_hmw__1

@job
def implnet_job_epa_hmw_hmw__1():
    harvest_epa_hmw_hmw__1()
