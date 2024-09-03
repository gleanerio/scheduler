from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_usbr_rise__0 import implnet_job_usbr_rise__0

@schedule(cron_schedule="0 0 25 * *", job=implnet_job_usbr_rise__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_usbr_rise__0(_context):
    run_config = {}
    return run_config
