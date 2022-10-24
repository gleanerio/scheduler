from dagster import schedule

from jobs.implnet_jobs_cuahsi150 import implnet_job_cuahsi150

@schedule(cron_schedule="0 11 * * 0", job=implnet_job_cuahsi150, execution_timezone="US/Central")
def implnet_sch_cuahsi150(_context):
    run_config = {}
    return run_config
