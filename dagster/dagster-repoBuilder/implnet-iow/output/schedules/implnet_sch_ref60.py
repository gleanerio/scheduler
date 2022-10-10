from dagster import schedule

from jobs.implnet_jobs_ref60 import implnet_job_ref60

@schedule(cron_schedule="0 13 * * 0", job=implnet_job_ref60, execution_timezone="US/Central")
def implnet_sch_ref60(_context):
    run_config = {}
    return run_config
