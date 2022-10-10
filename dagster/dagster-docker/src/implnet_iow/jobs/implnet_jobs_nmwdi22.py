from dagster import job

from ops.implnet_ops_nmwdi22 import harvest_nmwdi22

@job
def implnet_job_nmwdi22():
    harvest_nmwdi22()