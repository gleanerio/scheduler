from dagster import schedule

from jobs.implnet_jobs_cuahsi143 import implnet_job_cuahsi143

@schedule(cron_schedule="0 4 * * 0", job=implnet_job_cuahsi143, execution_timezone="US/Central")
def implnet_sch_cuahsi143(_context):
    run_config = {}
    return run_config
