from dagster import schedule

from jobs.implnet_jobs_cuahsihisdrwiids0 import implnet_job_cuahsihisdrwiids0

@schedule(cron_schedule="0 12 * * 5", job=implnet_job_cuahsihisdrwiids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisdrwiids0(_context):
    run_config = {}
    return run_config
