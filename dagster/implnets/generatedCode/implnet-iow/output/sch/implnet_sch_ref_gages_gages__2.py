from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_ref_gages_gages__2 import implnet_job_ref_gages_gages__2

@schedule(cron_schedule="0 6 27 * *", job=implnet_job_ref_gages_gages__2, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_ref_gages_gages__2(_context):
    run_config = {}
    return run_config
