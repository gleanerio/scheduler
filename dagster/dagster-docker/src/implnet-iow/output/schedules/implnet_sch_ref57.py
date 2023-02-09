from dagster import schedule

from jobs.implnet_jobs_ref57 import implnet_job_ref57

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_ref57, execution_timezone="US/Central")
def implnet_sch_ref57(_context):
    run_config = {}
    return run_config
