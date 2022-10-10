from dagster import schedule

from jobs.implnet_jobs_ref53 import implnet_job_ref53

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_ref53, execution_timezone="US/Central")
def implnet_sch_ref53(_context):
    run_config = {}
    return run_config
