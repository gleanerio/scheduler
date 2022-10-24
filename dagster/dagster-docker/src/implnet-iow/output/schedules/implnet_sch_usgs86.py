from dagster import schedule

from jobs.implnet_jobs_usgs86 import implnet_job_usgs86

@schedule(cron_schedule="0 16 * * 0", job=implnet_job_usgs86, execution_timezone="US/Central")
def implnet_sch_usgs86(_context):
    run_config = {}
    return run_config
