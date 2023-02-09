from dagster import schedule

from jobs.implnet_jobs_cuahsi120 import implnet_job_cuahsi120

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi120, execution_timezone="US/Central")
def implnet_sch_cuahsi120(_context):
    run_config = {}
    return run_config
