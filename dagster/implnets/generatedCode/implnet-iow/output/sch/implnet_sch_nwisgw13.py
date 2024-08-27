from dagster import schedule

from jobs.implnet_jobs_nwisgw13 import implnet_job_nwisgw13

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_nwisgw13, execution_timezone="US/Central")
def implnet_sch_nwisgw13(_context):
    run_config = {}
    return run_config
