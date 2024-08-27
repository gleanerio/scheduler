from dagster import schedule

from jobs.implnet_jobs_gages2 import implnet_job_gages2

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_gages2, execution_timezone="US/Central")
def implnet_sch_gages2(_context):
    run_config = {}
    return run_config
