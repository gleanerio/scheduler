from dagster import schedule

from jobs.implnet_jobs_cuahsi103 import implnet_job_cuahsi103

@schedule(cron_schedule="0 10 * * 0", job=implnet_job_cuahsi103, execution_timezone="US/Central")
def implnet_sch_cuahsi103(_context):
    run_config = {}
    return run_config
