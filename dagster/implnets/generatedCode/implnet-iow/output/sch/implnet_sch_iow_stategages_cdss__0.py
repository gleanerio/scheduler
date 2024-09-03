from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_iow_stategages_cdss__0 import implnet_job_iow_stategages_cdss__0

@schedule(cron_schedule="0 9 24 * *", job=implnet_job_iow_stategages_cdss__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_iow_stategages_cdss__0(_context):
    run_config = {}
    return run_config
