from dagster import schedule

from jobs.implnet_jobs_hu020 import implnet_job_hu020

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_hu020, execution_timezone="US/Central")
def implnet_sch_hu020(_context):
    run_config = {}
    return run_config
