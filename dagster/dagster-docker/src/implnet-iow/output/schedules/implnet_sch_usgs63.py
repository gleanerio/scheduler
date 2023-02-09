from dagster import schedule

from jobs.implnet_jobs_usgs63 import implnet_job_usgs63

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs63, execution_timezone="US/Central")
def implnet_sch_usgs63(_context):
    run_config = {}
    return run_config
