from dagster import schedule

from jobs.implnet_jobs_usgs90 import implnet_job_usgs90

@schedule(cron_schedule="0 20 * * 0", job=implnet_job_usgs90, execution_timezone="US/Central")
def implnet_sch_usgs90(_context):
    run_config = {}
    return run_config
