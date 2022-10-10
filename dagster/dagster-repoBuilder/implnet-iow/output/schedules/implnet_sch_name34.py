from dagster import schedule

from jobs.implnet_jobs_name34 import implnet_job_name34

@schedule(cron_schedule="0 10 * * 0", job=implnet_job_name34, execution_timezone="US/Central")
def implnet_sch_name34(_context):
    run_config = {}
    return run_config
