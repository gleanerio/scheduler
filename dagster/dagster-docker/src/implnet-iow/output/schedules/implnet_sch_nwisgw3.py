from dagster import schedule

from jobs.implnet_jobs_nwisgw3 import implnet_job_nwisgw3

@schedule(cron_schedule="0 6 * * 2", job=implnet_job_nwisgw3, execution_timezone="US/Central")
def implnet_sch_nwisgw3(_context):
    run_config = {}
    return run_config
