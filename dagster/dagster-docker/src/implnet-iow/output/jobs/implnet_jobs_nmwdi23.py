from dagster import job

from ops.implnet_ops_nmwdi23 import harvest_nmwdi23

@job
def implnet_job_nmwdi23():
    harvest_nmwdi23()