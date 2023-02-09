from dagster import schedule

from jobs.implnet_jobs_usgs83 import implnet_job_usgs83

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs83, execution_timezone="US/Central")
def implnet_sch_usgs83(_context):
    run_config = {}
    return run_config
