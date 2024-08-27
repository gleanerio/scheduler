from dagster import schedule

from jobs.implnet_jobs_nwisgw0 import implnet_job_nwisgw0

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_nwisgw0, execution_timezone="US/Central")
def implnet_sch_nwisgw0(_context):
    run_config = {}
    return run_config
