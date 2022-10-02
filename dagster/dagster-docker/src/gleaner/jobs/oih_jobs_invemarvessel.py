from dagster import job

from gleaner.ops.oih_invemarvessel import harvest_invemarvessel

@job
def oih_job_invemarvessel():
    harvest_invemarvessel()