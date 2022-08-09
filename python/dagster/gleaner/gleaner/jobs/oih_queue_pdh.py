from dagster import job

from gleaner.ops.queue_pdh import pdh

@job
def oih_queue_job_pdh():
    pdh()
