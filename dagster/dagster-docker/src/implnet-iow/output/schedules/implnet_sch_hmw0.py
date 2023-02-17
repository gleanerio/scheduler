from dagster import schedule

from jobs.implnet_jobs_hmw0 import implnet_job_hmw0

@schedule(cron_schedule="0 0 * * 4", job=implnet_job_hmw0, execution_timezone="US/Central")
def implnet_sch_hmw0(_context):
    run_config = {}
    return run_config
