from dagster import schedule

from jobs.implnet_jobs_usgs64 import implnet_job_usgs64

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs64, execution_timezone="US/Central")
def implnet_sch_usgs64(_context):
    run_config = {}
    return run_config
