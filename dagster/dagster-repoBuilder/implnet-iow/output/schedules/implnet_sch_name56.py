from dagster import schedule

from jobs.implnet_jobs_name56 import implnet_job_name56

@schedule(cron_schedule="0 9 * * 0", job=implnet_job_name56, execution_timezone="US/Central")
def implnet_sch_name56(_context):
    run_config = {}
    return run_config
