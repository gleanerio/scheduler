from dagster import schedule

from jobs.implnet_jobs_cuahsihisnevcanids0 import implnet_job_cuahsihisnevcanids0

@schedule(cron_schedule="0 15 * * 6", job=implnet_job_cuahsihisnevcanids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisnevcanids0(_context):
    run_config = {}
    return run_config
