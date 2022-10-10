from dagster import schedule

from jobs.implnet_jobs_usgs80 import implnet_job_usgs80

@schedule(cron_schedule="0 10 * * 0", job=implnet_job_usgs80, execution_timezone="US/Central")
def implnet_sch_usgs80(_context):
    run_config = {}
    return run_config
