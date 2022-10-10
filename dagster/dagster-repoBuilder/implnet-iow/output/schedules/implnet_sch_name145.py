from dagster import schedule

from jobs.implnet_jobs_name145 import implnet_job_name145

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_name145, execution_timezone="US/Central")
def implnet_sch_name145(_context):
    run_config = {}
    return run_config
