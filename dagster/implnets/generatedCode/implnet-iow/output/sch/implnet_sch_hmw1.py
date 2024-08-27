from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_hmw1 import implnet_job_hmw1

@schedule(cron_schedule="0 0 13 * *", job=implnet_job_hmw1, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_hmw1(_context):
    run_config = {}
    return run_config
