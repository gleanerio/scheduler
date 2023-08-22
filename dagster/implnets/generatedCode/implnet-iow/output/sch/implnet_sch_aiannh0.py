from dagster import schedule

from jobs.implnet_jobs_aiannh0 import implnet_job_aiannh0

@schedule(cron_schedule="0 8 24 * *", job=implnet_job_aiannh0, execution_timezone="US/Central")
def implnet_sch_aiannh0(_context):
    run_config = {}
    return run_config
