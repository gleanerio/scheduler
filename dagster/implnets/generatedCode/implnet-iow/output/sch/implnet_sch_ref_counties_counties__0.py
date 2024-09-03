from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_ref_counties_counties__0 import implnet_job_ref_counties_counties__0

@schedule(cron_schedule="0 0 26 * *", job=implnet_job_ref_counties_counties__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_ref_counties_counties__0(_context):
    run_config = {}
    return run_config
