from dagster import job

from ops.implnet_ops_chyldpilotids0 import harvest_chyldpilotids0

@job
def implnet_job_chyldpilotids0():
    harvest_chyldpilotids0()