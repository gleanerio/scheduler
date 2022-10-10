from dagster import job

from ops.implnet_ops_name13 import harvest_name13

@job
def implnet_job_name13():
    harvest_name13()