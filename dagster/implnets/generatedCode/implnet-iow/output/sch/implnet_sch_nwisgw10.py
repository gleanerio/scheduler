from dagster import schedule

from jobs.implnet_jobs_nwisgw10 import implnet_job_nwisgw10

@schedule(cron_schedule="0 4 2 * *", job=implnet_job_nwisgw10, execution_timezone="US/Central")
def implnet_sch_nwisgw10(_context):
    run_config = {}
    return run_config
