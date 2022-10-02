from dagster import job

from gleaner.ops.queue_cioos import harvest

@job
def oih_queue_job_cioos():
    harvest()

