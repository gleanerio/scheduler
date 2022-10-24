from dagster import schedule

from jobs.implnet_jobs_usgs85 import implnet_job_usgs85

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_usgs85, execution_timezone="US/Central")
def implnet_sch_usgs85(_context):
    run_config = {}
    return run_config
