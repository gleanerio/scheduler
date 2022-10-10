from dagster import schedule

from jobs.implnet_jobs_usgs91 import implnet_job_usgs91

@schedule(cron_schedule="0 21 * * 0", job=implnet_job_usgs91, execution_timezone="US/Central")
def implnet_sch_usgs91(_context):
    run_config = {}
    return run_config
