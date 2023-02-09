from dagster import schedule

from jobs.implnet_jobs_cuahsi153 import implnet_job_cuahsi153

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi153, execution_timezone="US/Central")
def implnet_sch_cuahsi153(_context):
    run_config = {}
    return run_config
