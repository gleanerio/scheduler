from dagster import schedule

from jobs.implnet_jobs_usgs94 import implnet_job_usgs94

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs94, execution_timezone="US/Central")
def implnet_sch_usgs94(_context):
    run_config = {}
    return run_config
