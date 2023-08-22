from dagster import schedule

from jobs.implnet_jobs_nwisgw1 import implnet_job_nwisgw1

@schedule(cron_schedule="0 8 4 * *", job=implnet_job_nwisgw1, execution_timezone="US/Central")
def implnet_sch_nwisgw1(_context):
    run_config = {}
    return run_config
