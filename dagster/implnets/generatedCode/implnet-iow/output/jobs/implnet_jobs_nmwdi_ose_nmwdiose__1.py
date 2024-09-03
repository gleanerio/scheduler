from dagster import job

from ops.implnet_ops_nmwdi_ose_nmwdiose__1 import harvest_nmwdi_ose_nmwdiose__1

@job
def implnet_job_nmwdi_ose_nmwdiose__1():
    harvest_nmwdi_ose_nmwdiose__1()
