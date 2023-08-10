from dagster import schedule

from jobs.implnet_jobs_hmw1 import implnet_job_hmw1

@schedule(cron_schedule="0 4 25 * *", job=implnet_job_hmw1, execution_timezone="US/Central")
def implnet_sch_hmw1(_context):
    run_config = {}
    return run_config
