from dagster import schedule

from jobs.implnet_jobs_name27 import implnet_job_name27

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_name27, execution_timezone="US/Central")
def implnet_sch_name27(_context):
    run_config = {}
    return run_config
