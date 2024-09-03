from dagster import job

from ops.implnet_ops_nmwdi_ose_nmwdiose__2 import harvest_nmwdi_ose_nmwdiose__2

@job
def implnet_job_nmwdi_ose_nmwdiose__2():
    harvest_nmwdi_ose_nmwdiose__2()
