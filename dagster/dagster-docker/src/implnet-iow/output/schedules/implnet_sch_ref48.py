from dagster import schedule

from jobs.implnet_jobs_ref48 import implnet_job_ref48

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_ref48, execution_timezone="US/Central")
def implnet_sch_ref48(_context):
    run_config = {}
    return run_config
