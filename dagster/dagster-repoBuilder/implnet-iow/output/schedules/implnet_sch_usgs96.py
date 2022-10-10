from dagster import schedule

from jobs.implnet_jobs_usgs96 import implnet_job_usgs96

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_usgs96, execution_timezone="US/Central")
def implnet_sch_usgs96(_context):
    run_config = {}
    return run_config
