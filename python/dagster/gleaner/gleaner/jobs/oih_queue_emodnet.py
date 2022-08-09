from dagster import job

from gleaner.ops.queue_emodnet import emodnet

@job
def oih_queue_job_emodnet():
    emodnet()
