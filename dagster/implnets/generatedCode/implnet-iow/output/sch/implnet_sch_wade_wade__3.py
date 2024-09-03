from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__3 import implnet_job_wade_wade__3

@schedule(cron_schedule="0 15 18 * *", job=implnet_job_wade_wade__3, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__3(_context):
    run_config = {}
    return run_config
