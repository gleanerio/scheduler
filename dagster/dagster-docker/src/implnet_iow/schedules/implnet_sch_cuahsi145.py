from dagster import schedule

from jobs.implnet_jobs_cuahsi145 import implnet_job_cuahsi145

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_cuahsi145, execution_timezone="US/Central")
def implnet_sch_cuahsi145(_context):
    run_config = {}
    return run_config
