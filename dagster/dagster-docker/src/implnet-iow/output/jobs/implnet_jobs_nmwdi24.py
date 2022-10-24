from dagster import job

from ops.implnet_ops_nmwdi24 import harvest_nmwdi24

@job
def implnet_job_nmwdi24():
    harvest_nmwdi24()