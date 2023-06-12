from dagster import schedule

from jobs.implnet_jobs_nwisgw2 import implnet_job_nwisgw2

@schedule(cron_schedule="0 3 * * 1", job=implnet_job_nwisgw2, execution_timezone="US/Central")
def implnet_sch_nwisgw2(_context):
    run_config = {}
    return run_config
