from dagster import schedule

from jobs.implnet_jobs_name10 import implnet_job_name10

@schedule(cron_schedule="0 9 * * 0", job=implnet_job_name10, execution_timezone="US/Central")
def implnet_sch_name10(_context):
    run_config = {}
    return run_config
