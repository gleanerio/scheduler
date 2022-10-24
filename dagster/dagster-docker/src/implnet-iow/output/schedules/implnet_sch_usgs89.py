from dagster import schedule

from jobs.implnet_jobs_usgs89 import implnet_job_usgs89

@schedule(cron_schedule="0 19 * * 0", job=implnet_job_usgs89, execution_timezone="US/Central")
def implnet_sch_usgs89(_context):
    run_config = {}
    return run_config
