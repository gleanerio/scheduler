from dagster import schedule

from jobs.implnet_jobs_ref61 import implnet_job_ref61

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_ref61, execution_timezone="US/Central")
def implnet_sch_ref61(_context):
    run_config = {}
    return run_config
