from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__5 import implnet_job_wade_wade__5

@schedule(cron_schedule="0 6 17 * *", job=implnet_job_wade_wade__5, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__5(_context):
    run_config = {}
    return run_config
