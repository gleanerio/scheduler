from dagster import job

from ops.implnet_ops_chyld1 import harvest_chyld1

@job
def implnet_job_chyld1():
    harvest_chyld1()