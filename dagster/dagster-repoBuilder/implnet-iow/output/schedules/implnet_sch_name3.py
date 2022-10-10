from dagster import schedule

from jobs.implnet_jobs_name3 import implnet_job_name3

@schedule(cron_schedule="0 2 * * 0", job=implnet_job_name3, execution_timezone="US/Central")
def implnet_sch_name3(_context):
    run_config = {}
    return run_config
