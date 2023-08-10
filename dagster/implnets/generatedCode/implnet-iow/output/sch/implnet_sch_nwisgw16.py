from dagster import schedule

from jobs.implnet_jobs_nwisgw16 import implnet_job_nwisgw16

@schedule(cron_schedule="0 8 1 * *", job=implnet_job_nwisgw16, execution_timezone="US/Central")
def implnet_sch_nwisgw16(_context):
    run_config = {}
    return run_config
