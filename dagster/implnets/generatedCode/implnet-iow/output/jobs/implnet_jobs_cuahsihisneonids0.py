from dagster import job

from ops.implnet_ops_cuahsihisneonids0 import harvest_cuahsihisneonids0

@job
def implnet_job_cuahsihisneonids0():
    harvest_cuahsihisneonids0()