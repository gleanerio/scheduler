from dagster import job

from ops.implnet_ops_emodnet import harvest_emodnet

@job
def implnet_job_emodnet():
    harvest_emodnet()