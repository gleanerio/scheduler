from dagster import schedule

from jobs.implnet_jobs_name108 import implnet_job_name108

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_name108, execution_timezone="US/Central")
def implnet_sch_name108(_context):
    run_config = {}
    return run_config
