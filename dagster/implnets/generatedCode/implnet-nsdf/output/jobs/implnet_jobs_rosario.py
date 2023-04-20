from dagster import job

from ops.implnet_ops_rosario import harvest_rosario

@job
def implnet_job_rosario():
    harvest_rosario()