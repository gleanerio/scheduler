from dagster import job

from ops.implnet_ops_hu040 import harvest_hu040

@job
def implnet_job_hu040():
    harvest_hu040()