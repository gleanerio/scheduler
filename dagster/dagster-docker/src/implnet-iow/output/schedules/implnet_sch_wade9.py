from dagster import schedule

from jobs.implnet_jobs_wade9 import implnet_job_wade9

@schedule(cron_schedule="0 12 * * 6", job=implnet_job_wade9, execution_timezone="US/Central")
def implnet_sch_wade9(_context):
    run_config = {}
    return run_config
