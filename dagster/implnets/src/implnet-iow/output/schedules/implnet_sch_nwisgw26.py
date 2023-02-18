from dagster import schedule

from jobs.implnet_jobs_nwisgw26 import implnet_job_nwisgw26

@schedule(cron_schedule="0 18 * * 1", job=implnet_job_nwisgw26, execution_timezone="US/Central")
def implnet_sch_nwisgw26(_context):
    run_config = {}
    return run_config
