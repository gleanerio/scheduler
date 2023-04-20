from dagster import job

from ops.implnet_ops_resourceregistry import harvest_resourceregistry

@job
def implnet_job_resourceregistry():
    harvest_resourceregistry()