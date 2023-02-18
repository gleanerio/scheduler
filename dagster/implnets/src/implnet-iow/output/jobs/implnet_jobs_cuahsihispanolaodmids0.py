from dagster import job

from ops.implnet_ops_cuahsihispanolaodmids0 import harvest_cuahsihispanolaodmids0

@job
def implnet_job_cuahsihispanolaodmids0():
    harvest_cuahsihispanolaodmids0()