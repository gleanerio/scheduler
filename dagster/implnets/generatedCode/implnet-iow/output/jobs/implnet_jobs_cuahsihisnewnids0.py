from dagster import job

from ops.implnet_ops_cuahsihisnewnids0 import harvest_cuahsihisnewnids0

@job
def implnet_job_cuahsihisnewnids0():
    harvest_cuahsihisnewnids0()