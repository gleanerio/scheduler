from dagster import schedule

from jobs.implnet_jobs_usgs82 import implnet_job_usgs82

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs82, execution_timezone="US/Central")
def implnet_sch_usgs82(_context):
    run_config = {}
    return run_config
