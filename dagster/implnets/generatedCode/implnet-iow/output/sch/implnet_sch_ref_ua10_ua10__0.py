from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_ref_ua10_ua10__0 import implnet_job_ref_ua10_ua10__0

@schedule(cron_schedule="0 18 26 * *", job=implnet_job_ref_ua10_ua10__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_ref_ua10_ua10__0(_context):
    run_config = {}
    return run_config
