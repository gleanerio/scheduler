from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__17 import implnet_job_wade_wade__17

@schedule(cron_schedule="0 3 13 * *", job=implnet_job_wade_wade__17, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__17(_context):
    run_config = {}
    return run_config
