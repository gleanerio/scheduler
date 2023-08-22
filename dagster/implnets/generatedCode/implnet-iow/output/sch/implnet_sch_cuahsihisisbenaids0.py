from dagster import schedule

from jobs.implnet_jobs_cuahsihisisbenaids0 import implnet_job_cuahsihisisbenaids0

@schedule(cron_schedule="0 0 20 * *", job=implnet_job_cuahsihisisbenaids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisisbenaids0(_context):
    run_config = {}
    return run_config
