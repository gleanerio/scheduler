from dagster import schedule

from jobs.implnet_jobs_nwisgw15 import implnet_job_nwisgw15

@schedule(cron_schedule="0 0 * * 1", job=implnet_job_nwisgw15, execution_timezone="US/Central")
def implnet_sch_nwisgw15(_context):
    run_config = {}
    return run_config
