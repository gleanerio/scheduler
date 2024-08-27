from dagster import schedule

from jobs.implnet_jobs_wade29 import implnet_job_wade29

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_wade29, execution_timezone="US/Central")
def implnet_sch_wade29(_context):
    run_config = {}
    return run_config
