from dagster import job

from ops.implnet_ops_usbr_rise__0 import harvest_usbr_rise__0

@job
def implnet_job_usbr_rise__0():
    harvest_usbr_rise__0()
