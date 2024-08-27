from dagster import schedule

from jobs.implnet_jobs_cuahsihisghcnids0 import implnet_job_cuahsihisghcnids0

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_cuahsihisghcnids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisghcnids0(_context):
    run_config = {}
    return run_config
