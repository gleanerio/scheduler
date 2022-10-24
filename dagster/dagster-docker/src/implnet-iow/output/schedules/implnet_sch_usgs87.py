from dagster import schedule

from jobs.implnet_jobs_usgs87 import implnet_job_usgs87

@schedule(cron_schedule="0 17 * * 0", job=implnet_job_usgs87, execution_timezone="US/Central")
def implnet_sch_usgs87(_context):
    run_config = {}
    return run_config
