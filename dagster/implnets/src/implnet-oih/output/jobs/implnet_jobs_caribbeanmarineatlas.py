from dagster import job

from ops.implnet_ops_caribbeanmarineatlas import harvest_caribbeanmarineatlas

@job
def implnet_job_caribbeanmarineatlas():
    harvest_caribbeanmarineatlas()