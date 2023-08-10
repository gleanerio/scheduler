from dagster import schedule

from jobs.implnet_jobs_nwisgw18 import implnet_job_nwisgw18

@schedule(cron_schedule="0 4 5 * *", job=implnet_job_nwisgw18, execution_timezone="US/Central")
def implnet_sch_nwisgw18(_context):
    run_config = {}
    return run_config
