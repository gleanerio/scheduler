from dagster import job

from ops.implnet_ops_sechydrgreg0 import harvest_sechydrgreg0

@job
def implnet_job_sechydrgreg0():
    harvest_sechydrgreg0()