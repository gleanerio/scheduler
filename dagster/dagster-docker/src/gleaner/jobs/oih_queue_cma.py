from dagster import job

from gleaner.ops.queue_cma import cma

@job
def oih_queue_job_cma():
    cma()
