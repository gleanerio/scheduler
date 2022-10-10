from dagster import schedule

from jobs.implnet_jobs_name162 import implnet_job_name162

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_name162, execution_timezone="US/Central")
def implnet_sch_name162(_context):
    run_config = {}
    return run_config
