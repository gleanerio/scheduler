from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_gages2 import implnet_job_gages2

@schedule(cron_schedule="0 12 4 * *", job=implnet_job_gages2, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_gages2(_context):
    run_config = {}
    return run_config
