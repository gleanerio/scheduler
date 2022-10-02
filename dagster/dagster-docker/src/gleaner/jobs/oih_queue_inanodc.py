from dagster import job

from gleaner.ops.queue_inanodc import inanodc

@job
def oih_queue_job_inanodc():
    inanodc()
