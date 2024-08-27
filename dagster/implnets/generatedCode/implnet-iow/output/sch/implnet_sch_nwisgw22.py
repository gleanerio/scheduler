from dagster import schedule

from jobs.implnet_jobs_nwisgw22 import implnet_job_nwisgw22

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_nwisgw22, execution_timezone="US/Central")
def implnet_sch_nwisgw22(_context):
    run_config = {}
    return run_config
