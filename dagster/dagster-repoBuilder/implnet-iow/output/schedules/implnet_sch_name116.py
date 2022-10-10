from dagster import schedule

from jobs.implnet_jobs_name116 import implnet_job_name116

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_name116, execution_timezone="US/Central")
def implnet_sch_name116(_context):
    run_config = {}
    return run_config
