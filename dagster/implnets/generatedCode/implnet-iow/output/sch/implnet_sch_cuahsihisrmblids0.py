from dagster import schedule

from jobs.implnet_jobs_cuahsihisrmblids0 import implnet_job_cuahsihisrmblids0

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_cuahsihisrmblids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisrmblids0(_context):
    run_config = {}
    return run_config
