from dagster import job

from ops.implnet_ops_cagagespids0 import harvest_cagagespids0

@job
def implnet_job_cagagespids0():
    harvest_cagagespids0()