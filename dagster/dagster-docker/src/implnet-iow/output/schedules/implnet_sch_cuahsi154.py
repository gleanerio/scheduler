from dagster import schedule

from jobs.implnet_jobs_cuahsi154 import implnet_job_cuahsi154

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi154, execution_timezone="US/Central")
def implnet_sch_cuahsi154(_context):
    run_config = {}
    return run_config
