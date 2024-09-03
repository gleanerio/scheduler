from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__38 import implnet_job_wade_wade__38

@schedule(cron_schedule="0 12 18 * *", job=implnet_job_wade_wade__38, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__38(_context):
    run_config = {}
    return run_config
