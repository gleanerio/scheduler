from dagster import schedule

from jobs.implnet_jobs_name24 import implnet_job_name24

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_name24, execution_timezone="US/Central")
def implnet_sch_name24(_context):
    run_config = {}
    return run_config
