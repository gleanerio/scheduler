from dagster import schedule

from jobs.implnet_jobs_usgs88 import implnet_job_usgs88

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs88, execution_timezone="US/Central")
def implnet_sch_usgs88(_context):
    run_config = {}
    return run_config
