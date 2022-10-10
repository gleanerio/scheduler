from dagster import schedule

from jobs.implnet_jobs_name175 import implnet_job_name175

@schedule(cron_schedule="0 13 * * 0", job=implnet_job_name175, execution_timezone="US/Central")
def implnet_sch_name175(_context):
    run_config = {}
    return run_config
