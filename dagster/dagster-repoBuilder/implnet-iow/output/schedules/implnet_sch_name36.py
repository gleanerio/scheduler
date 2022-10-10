from dagster import schedule

from jobs.implnet_jobs_name36 import implnet_job_name36

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_name36, execution_timezone="US/Central")
def implnet_sch_name36(_context):
    run_config = {}
    return run_config
