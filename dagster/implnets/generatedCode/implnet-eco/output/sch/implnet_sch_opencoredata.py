from dagster import schedule

from jobs.implnet_jobs_opencoredata import implnet_job_opencoredata

@schedule(cron_schedule="0 0 5 * *", job=implnet_job_opencoredata, execution_timezone="US/Central")
def implnet_sch_opencoredata(_context):
    run_config = {}
    return run_config
