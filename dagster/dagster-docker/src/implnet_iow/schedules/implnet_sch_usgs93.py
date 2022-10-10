from dagster import schedule

from jobs.implnet_jobs_usgs93 import implnet_job_usgs93

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs93, execution_timezone="US/Central")
def implnet_sch_usgs93(_context):
    run_config = {}
    return run_config
