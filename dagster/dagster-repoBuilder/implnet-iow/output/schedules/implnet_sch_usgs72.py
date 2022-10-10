from dagster import schedule

from jobs.implnet_jobs_usgs72 import implnet_job_usgs72

@schedule(cron_schedule="0 2 * * 0", job=implnet_job_usgs72, execution_timezone="US/Central")
def implnet_sch_usgs72(_context):
    run_config = {}
    return run_config
