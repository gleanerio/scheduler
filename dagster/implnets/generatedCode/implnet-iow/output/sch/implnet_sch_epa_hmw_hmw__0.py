from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_epa_hmw_hmw__0 import implnet_job_epa_hmw_hmw__0

@schedule(cron_schedule="0 21 18 * *", job=implnet_job_epa_hmw_hmw__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_epa_hmw_hmw__0(_context):
    run_config = {}
    return run_config
