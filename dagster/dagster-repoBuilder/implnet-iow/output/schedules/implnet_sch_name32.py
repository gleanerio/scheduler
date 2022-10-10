from dagster import schedule

from jobs.implnet_jobs_name32 import implnet_job_name32

@schedule(cron_schedule="0 8 * * 0", job=implnet_job_name32, execution_timezone="US/Central")
def implnet_sch_name32(_context):
    run_config = {}
    return run_config
