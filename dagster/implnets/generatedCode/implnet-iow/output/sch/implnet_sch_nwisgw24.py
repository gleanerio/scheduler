from dagster import schedule

from jobs.implnet_jobs_nwisgw24 import implnet_job_nwisgw24

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_nwisgw24, execution_timezone="US/Central")
def implnet_sch_nwisgw24(_context):
    run_config = {}
    return run_config
