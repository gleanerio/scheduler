from dagster import schedule

from jobs.implnet_jobs_cuahsi142 import implnet_job_cuahsi142

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi142, execution_timezone="US/Central")
def implnet_sch_cuahsi142(_context):
    run_config = {}
    return run_config
