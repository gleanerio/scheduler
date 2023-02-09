from dagster import schedule

from jobs.implnet_jobs_usgs66 import implnet_job_usgs66

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs66, execution_timezone="US/Central")
def implnet_sch_usgs66(_context):
    run_config = {}
    return run_config
