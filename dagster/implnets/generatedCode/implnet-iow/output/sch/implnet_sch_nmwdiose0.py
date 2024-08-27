from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_nmwdiose0 import implnet_job_nmwdiose0

@schedule(cron_schedule="0 0 26 * *", job=implnet_job_nmwdiose0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_nmwdiose0(_context):
    run_config = {}
    return run_config
