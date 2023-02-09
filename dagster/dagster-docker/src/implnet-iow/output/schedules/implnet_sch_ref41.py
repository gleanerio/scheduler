from dagster import schedule

from jobs.implnet_jobs_ref41 import implnet_job_ref41

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_ref41, execution_timezone="US/Central")
def implnet_sch_ref41(_context):
    run_config = {}
    return run_config
