from dagster import job

from ops.implnet_ops_benguelacc import harvest_benguelacc

@job
def implnet_job_benguelacc():
    harvest_benguelacc()