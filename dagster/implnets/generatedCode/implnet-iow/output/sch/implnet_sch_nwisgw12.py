from dagster import schedule

from jobs.implnet_jobs_nwisgw12 import implnet_job_nwisgw12

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_nwisgw12, execution_timezone="US/Central")
def implnet_sch_nwisgw12(_context):
    run_config = {}
    return run_config
