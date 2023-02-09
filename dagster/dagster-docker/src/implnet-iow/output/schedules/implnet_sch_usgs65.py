from dagster import schedule

from jobs.implnet_jobs_usgs65 import implnet_job_usgs65

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs65, execution_timezone="US/Central")
def implnet_sch_usgs65(_context):
    run_config = {}
    return run_config
