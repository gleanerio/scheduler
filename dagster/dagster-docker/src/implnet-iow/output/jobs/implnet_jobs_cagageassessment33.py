from dagster import job

from ops.implnet_ops_cagageassessment33 import harvest_cagageassessment33

@job
def implnet_job_cagageassessment33():
    harvest_cagageassessment33()