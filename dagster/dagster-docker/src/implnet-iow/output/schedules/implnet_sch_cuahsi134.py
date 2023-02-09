from dagster import schedule

from jobs.implnet_jobs_cuahsi134 import implnet_job_cuahsi134

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi134, execution_timezone="US/Central")
def implnet_sch_cuahsi134(_context):
    run_config = {}
    return run_config
