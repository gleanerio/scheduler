from dagster import schedule

from jobs.implnet_jobs_ref46 import implnet_job_ref46

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_ref46, execution_timezone="US/Central")
def implnet_sch_ref46(_context):
    run_config = {}
    return run_config
