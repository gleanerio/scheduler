from dagster import schedule

from jobs.implnet_jobs_nwisgw8 import implnet_job_nwisgw8

@schedule(cron_schedule="0 21 * * 2", job=implnet_job_nwisgw8, execution_timezone="US/Central")
def implnet_sch_nwisgw8(_context):
    run_config = {}
    return run_config
