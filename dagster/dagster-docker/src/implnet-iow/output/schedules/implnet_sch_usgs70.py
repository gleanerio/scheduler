from dagster import schedule

from jobs.implnet_jobs_usgs70 import implnet_job_usgs70

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs70, execution_timezone="US/Central")
def implnet_sch_usgs70(_context):
    run_config = {}
    return run_config
