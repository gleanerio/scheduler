from dagster import schedule

from jobs.implnet_jobs_cuahsi147 import implnet_job_cuahsi147

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi147, execution_timezone="US/Central")
def implnet_sch_cuahsi147(_context):
    run_config = {}
    return run_config
