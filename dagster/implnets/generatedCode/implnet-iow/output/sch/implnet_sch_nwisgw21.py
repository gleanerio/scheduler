from dagster import schedule

from jobs.implnet_jobs_nwisgw21 import implnet_job_nwisgw21

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_nwisgw21, execution_timezone="US/Central")
def implnet_sch_nwisgw21(_context):
    run_config = {}
    return run_config
