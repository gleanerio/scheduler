from dagster import schedule

from jobs.implnet_jobs_usgs79 import implnet_job_usgs79

@schedule(cron_schedule="0 9 * * 0", job=implnet_job_usgs79, execution_timezone="US/Central")
def implnet_sch_usgs79(_context):
    run_config = {}
    return run_config
