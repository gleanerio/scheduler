from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_chyld_chyldpilot_ids__0 import implnet_job_chyld_chyldpilot_ids__0

@schedule(cron_schedule="0 12 11 * *", job=implnet_job_chyld_chyldpilot_ids__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_chyld_chyldpilot_ids__0(_context):
    run_config = {}
    return run_config
