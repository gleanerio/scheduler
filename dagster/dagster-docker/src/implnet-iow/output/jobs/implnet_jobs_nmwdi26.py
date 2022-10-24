from dagster import job

from ops.implnet_ops_nmwdi26 import harvest_nmwdi26

@job
def implnet_job_nmwdi26():
    harvest_nmwdi26()