from dagster import schedule

from jobs.implnet_jobs_name53 import implnet_job_name53

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_name53, execution_timezone="US/Central")
def implnet_sch_name53(_context):
    run_config = {}
    return run_config
