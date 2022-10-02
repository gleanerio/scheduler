from dagster import job

from gleaner.ops.implnet_invemarvessel import harvest_invemarvessel

@job
def implnet_job_invemarvessel():
    harvest_invemarvessel()