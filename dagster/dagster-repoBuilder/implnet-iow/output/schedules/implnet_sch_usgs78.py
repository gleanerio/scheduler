from dagster import schedule

from jobs.implnet_jobs_usgs78 import implnet_job_usgs78

@schedule(cron_schedule="0 8 * * 0", job=implnet_job_usgs78, execution_timezone="US/Central")
def implnet_sch_usgs78(_context):
    run_config = {}
    return run_config
