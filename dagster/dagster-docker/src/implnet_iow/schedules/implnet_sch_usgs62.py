from dagster import schedule

from jobs.implnet_jobs_usgs62 import implnet_job_usgs62

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_usgs62, execution_timezone="US/Central")
def implnet_sch_usgs62(_context):
    run_config = {}
    return run_config
