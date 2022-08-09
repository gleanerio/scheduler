from dagster import job

from gleaner.ops.queue_pogo import pogo

@job
def oih_queue_job_pogo():
    pogo()
