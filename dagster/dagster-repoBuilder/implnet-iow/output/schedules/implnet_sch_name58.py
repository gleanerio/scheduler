from dagster import schedule

from jobs.implnet_jobs_name58 import implnet_job_name58

@schedule(cron_schedule="0 11 * * 0", job=implnet_job_name58, execution_timezone="US/Central")
def implnet_sch_name58(_context):
    run_config = {}
    return run_config
