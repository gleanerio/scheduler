from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_epa_hmw_hmw__1 import implnet_job_epa_hmw_hmw__1

@schedule(cron_schedule="0 0 19 * *", job=implnet_job_epa_hmw_hmw__1, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_epa_hmw_hmw__1(_context):
    run_config = {}
    return run_config
