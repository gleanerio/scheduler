from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_usgs_hydrologicunit__0 import implnet_job_usgs_hydrologicunit__0

@schedule(cron_schedule="0 6 19 * *", job=implnet_job_usgs_hydrologicunit__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_usgs_hydrologicunit__0(_context):
    run_config = {}
    return run_config
