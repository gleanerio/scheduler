from dagster import schedule

from jobs.implnet_jobs_name20 import implnet_job_name20

@schedule(cron_schedule="0 19 * * 0", job=implnet_job_name20, execution_timezone="US/Central")
def implnet_sch_name20(_context):
    run_config = {}
    return run_config
