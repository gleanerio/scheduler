from dagster import schedule

from jobs.implnet_jobs_wade15 import implnet_job_wade15

@schedule(cron_schedule="0 21 * * 6", job=implnet_job_wade15, execution_timezone="US/Central")
def implnet_sch_wade15(_context):
    run_config = {}
    return run_config
