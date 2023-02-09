from dagster import schedule

from jobs.implnet_jobs_usgs68 import implnet_job_usgs68

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs68, execution_timezone="US/Central")
def implnet_sch_usgs68(_context):
    run_config = {}
    return run_config
