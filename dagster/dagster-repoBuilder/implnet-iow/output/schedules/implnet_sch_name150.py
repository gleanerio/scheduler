from dagster import schedule

from jobs.implnet_jobs_name150 import implnet_job_name150

@schedule(cron_schedule="0 11 * * 0", job=implnet_job_name150, execution_timezone="US/Central")
def implnet_sch_name150(_context):
    run_config = {}
    return run_config
