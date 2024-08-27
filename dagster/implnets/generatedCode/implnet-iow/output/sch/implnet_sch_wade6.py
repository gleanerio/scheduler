from dagster import schedule

from jobs.implnet_jobs_wade6 import implnet_job_wade6

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_wade6, execution_timezone="US/Central")
def implnet_sch_wade6(_context):
    run_config = {}
    return run_config
