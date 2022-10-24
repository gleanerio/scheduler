from dagster import schedule

from jobs.implnet_jobs_usgs75 import implnet_job_usgs75

@schedule(cron_schedule="0 5 * * 0", job=implnet_job_usgs75, execution_timezone="US/Central")
def implnet_sch_usgs75(_context):
    run_config = {}
    return run_config
