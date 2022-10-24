from dagster import job

from ops.implnet_ops_nmwdi25 import harvest_nmwdi25

@job
def implnet_job_nmwdi25():
    harvest_nmwdi25()