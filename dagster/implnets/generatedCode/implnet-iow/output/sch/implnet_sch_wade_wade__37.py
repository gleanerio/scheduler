from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__37 import implnet_job_wade_wade__37

@schedule(cron_schedule="0 15 16 * *", job=implnet_job_wade_wade__37, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__37(_context):
    run_config = {}
    return run_config
