from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__21 import implnet_job_wade_wade__21

@schedule(cron_schedule="0 12 14 * *", job=implnet_job_wade_wade__21, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__21(_context):
    run_config = {}
    return run_config
