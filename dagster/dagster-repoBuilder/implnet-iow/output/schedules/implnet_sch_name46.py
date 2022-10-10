from dagster import schedule

from jobs.implnet_jobs_name46 import implnet_job_name46

@schedule(cron_schedule="0 22 * * 0", job=implnet_job_name46, execution_timezone="US/Central")
def implnet_sch_name46(_context):
    run_config = {}
    return run_config
