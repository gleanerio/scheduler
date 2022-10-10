from dagster import schedule

from jobs.implnet_jobs_name129 import implnet_job_name129

@schedule(cron_schedule="0 13 * * 0", job=implnet_job_name129, execution_timezone="US/Central")
def implnet_sch_name129(_context):
    run_config = {}
    return run_config
