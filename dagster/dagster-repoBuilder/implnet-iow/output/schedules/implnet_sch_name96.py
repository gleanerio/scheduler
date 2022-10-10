from dagster import schedule

from jobs.implnet_jobs_name96 import implnet_job_name96

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_name96, execution_timezone="US/Central")
def implnet_sch_name96(_context):
    run_config = {}
    return run_config
