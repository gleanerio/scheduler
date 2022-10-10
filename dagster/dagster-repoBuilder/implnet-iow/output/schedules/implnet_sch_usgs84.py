from dagster import schedule

from jobs.implnet_jobs_usgs84 import implnet_job_usgs84

@schedule(cron_schedule="0 14 * * 0", job=implnet_job_usgs84, execution_timezone="US/Central")
def implnet_sch_usgs84(_context):
    run_config = {}
    return run_config
