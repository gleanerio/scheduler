from dagster import job

from ops.implnet_ops_milano import harvest_milano

@job
def implnet_job_milano():
    harvest_milano()