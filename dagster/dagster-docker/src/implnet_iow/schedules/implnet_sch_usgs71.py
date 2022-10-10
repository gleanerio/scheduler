from dagster import schedule

from jobs.implnet_jobs_usgs71 import implnet_job_usgs71

@schedule(cron_schedule="0 1 * * 0", job=implnet_job_usgs71, execution_timezone="US/Central")
def implnet_sch_usgs71(_context):
    run_config = {}
    return run_config
