from dagster import job

from gleaner.ops.queue_maspawio import maspawio

@job
def oih_queue_job_maspawio():
    maspawio()
