from dagster import schedule

from jobs.implnet_jobs_name126 import implnet_job_name126

@schedule(cron_schedule="0 10 * * 0", job=implnet_job_name126, execution_timezone="US/Central")
def implnet_sch_name126(_context):
    run_config = {}
    return run_config
