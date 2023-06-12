from dagster import job

from ops.implnet_ops_cuahsihisscanids0 import harvest_cuahsihisscanids0

@job
def implnet_job_cuahsihisscanids0():
    harvest_cuahsihisscanids0()