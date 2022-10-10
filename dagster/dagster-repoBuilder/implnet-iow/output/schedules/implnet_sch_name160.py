from dagster import schedule

from jobs.implnet_jobs_name160 import implnet_job_name160

@schedule(cron_schedule="0 21 * * 0", job=implnet_job_name160, execution_timezone="US/Central")
def implnet_sch_name160(_context):
    run_config = {}
    return run_config
