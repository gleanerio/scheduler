from dagster import schedule

from jobs.implnet_jobs_usgs76 import implnet_job_usgs76

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs76, execution_timezone="US/Central")
def implnet_sch_usgs76(_context):
    run_config = {}
    return run_config
