from dagster import schedule

from jobs.implnet_jobs_cuahsi140 import implnet_job_cuahsi140

@schedule(cron_schedule="0 1 * * 0", job=implnet_job_cuahsi140, execution_timezone="US/Central")
def implnet_sch_cuahsi140(_context):
    run_config = {}
    return run_config
