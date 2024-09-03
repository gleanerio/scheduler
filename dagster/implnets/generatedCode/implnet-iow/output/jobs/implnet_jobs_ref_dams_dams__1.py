from dagster import job

from ops.implnet_ops_ref_dams_dams__1 import harvest_ref_dams_dams__1

@job
def implnet_job_ref_dams_dams__1():
    harvest_ref_dams_dams__1()
