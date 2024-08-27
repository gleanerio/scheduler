from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_hu100 import implnet_job_hu100

@schedule(cron_schedule="0 4 24 * *", job=implnet_job_hu100, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_hu100(_context):
    run_config = {}
    return run_config
