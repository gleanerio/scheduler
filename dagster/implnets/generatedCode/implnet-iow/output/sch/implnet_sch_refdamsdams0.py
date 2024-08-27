from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_refdamsdams0 import implnet_job_refdamsdams0

@schedule(cron_schedule="0 6 3 * *", job=implnet_job_refdamsdams0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_refdamsdams0(_context):
    run_config = {}
    return run_config
