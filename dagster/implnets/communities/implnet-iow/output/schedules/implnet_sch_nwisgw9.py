from dagster import schedule

from jobs.implnet_jobs_nwisgw9 import implnet_job_nwisgw9

@schedule(cron_schedule="0 9 * * 1", job=implnet_job_nwisgw9, execution_timezone="US/Central")
def implnet_sch_nwisgw9(_context):
    run_config = {}
    return run_config
