from dagster import schedule

from jobs.implnet_jobs_name85 import implnet_job_name85

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_name85, execution_timezone="US/Central")
def implnet_sch_name85(_context):
    run_config = {}
    return run_config
