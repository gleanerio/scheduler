from dagster import schedule

from jobs.implnet_jobs_cuahsihislittlebearriverids0 import implnet_job_cuahsihislittlebearriverids0

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_cuahsihislittlebearriverids0, execution_timezone="US/Central")
def implnet_sch_cuahsihislittlebearriverids0(_context):
    run_config = {}
    return run_config
