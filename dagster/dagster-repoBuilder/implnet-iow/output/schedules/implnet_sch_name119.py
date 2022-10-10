from dagster import schedule

from jobs.implnet_jobs_name119 import implnet_job_name119

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_name119, execution_timezone="US/Central")
def implnet_sch_name119(_context):
    run_config = {}
    return run_config
