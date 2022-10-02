from dagster import job

from gleaner.ops.queue_benguelacc import benguelacc

@job
def oih_queue_job_benguelacc():
    benguelacc()
