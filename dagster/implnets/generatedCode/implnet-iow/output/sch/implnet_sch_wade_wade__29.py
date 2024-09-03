from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__29 import implnet_job_wade_wade__29

@schedule(cron_schedule="0 3 17 * *", job=implnet_job_wade_wade__29, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__29(_context):
    run_config = {}
    return run_config
