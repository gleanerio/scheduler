from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__0 import implnet_job_wade_wade__0

@schedule(cron_schedule="0 18 12 * *", job=implnet_job_wade_wade__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__0(_context):
    run_config = {}
    return run_config
