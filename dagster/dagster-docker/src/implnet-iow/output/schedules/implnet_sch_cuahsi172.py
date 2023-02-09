from dagster import schedule

from jobs.implnet_jobs_cuahsi172 import implnet_job_cuahsi172

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi172, execution_timezone="US/Central")
def implnet_sch_cuahsi172(_context):
    run_config = {}
    return run_config
