from dagster import job

from ops.implnet_ops_invemarvessel import harvest_invemarvessel

@job
def implnet_job_invemarvessel():
    harvest_invemarvessel()