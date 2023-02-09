from dagster import schedule

from jobs.implnet_jobs_usgs81 import implnet_job_usgs81

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs81, execution_timezone="US/Central")
def implnet_sch_usgs81(_context):
    run_config = {}
    return run_config
