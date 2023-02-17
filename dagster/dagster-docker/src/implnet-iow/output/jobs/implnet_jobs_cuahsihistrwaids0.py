from dagster import job

from ops.implnet_ops_cuahsihistrwaids0 import harvest_cuahsihistrwaids0

@job
def implnet_job_cuahsihistrwaids0():
    harvest_cuahsihistrwaids0()