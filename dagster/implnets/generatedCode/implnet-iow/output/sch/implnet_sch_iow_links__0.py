from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_iow_links__0 import implnet_job_iow_links__0

@schedule(cron_schedule="0 21 23 * *", job=implnet_job_iow_links__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_iow_links__0(_context):
    run_config = {}
    return run_config
