from dagster import schedule

from jobs.implnet_jobs_counties0 import implnet_job_counties0

@schedule(cron_schedule="0 9 * * 1", job=implnet_job_counties0, execution_timezone="US/Central")
def implnet_sch_counties0(_context):
    run_config = {}
    return run_config
