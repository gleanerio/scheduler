from dagster import job

from ops.implnet_ops_nmwdi27 import harvest_nmwdi27

@job
def implnet_job_nmwdi27():
    harvest_nmwdi27()