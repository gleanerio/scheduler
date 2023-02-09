from dagster import schedule

from jobs.implnet_jobs_usgs97 import implnet_job_usgs97

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs97, execution_timezone="US/Central")
def implnet_sch_usgs97(_context):
    run_config = {}
    return run_config
