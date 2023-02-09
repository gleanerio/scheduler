from dagster import schedule

from jobs.implnet_jobs_usgs73 import implnet_job_usgs73

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs73, execution_timezone="US/Central")
def implnet_sch_usgs73(_context):
    run_config = {}
    return run_config
