from dagster import schedule

from jobs.implnet_jobs_nwisgw14 import implnet_job_nwisgw14

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_nwisgw14, execution_timezone="US/Central")
def implnet_sch_nwisgw14(_context):
    run_config = {}
    return run_config
