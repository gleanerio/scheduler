from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_dams1 import implnet_job_dams1

@schedule(cron_schedule="0 16 23 * *", job=implnet_job_dams1, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_dams1(_context):
    run_config = {}
    return run_config
