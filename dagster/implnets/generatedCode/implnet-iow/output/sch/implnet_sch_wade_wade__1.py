from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__1 import implnet_job_wade_wade__1

@schedule(cron_schedule="0 3 16 * *", job=implnet_job_wade_wade__1, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__1(_context):
    run_config = {}
    return run_config
