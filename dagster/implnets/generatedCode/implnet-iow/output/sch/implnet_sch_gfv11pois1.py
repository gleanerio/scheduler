from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_gfv11pois1 import implnet_job_gfv11pois1

@schedule(cron_schedule="0 12 6 * *", job=implnet_job_gfv11pois1, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_gfv11pois1(_context):
    run_config = {}
    return run_config
