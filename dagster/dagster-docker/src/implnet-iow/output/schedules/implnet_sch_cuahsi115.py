from dagster import schedule

from jobs.implnet_jobs_cuahsi115 import implnet_job_cuahsi115

@schedule(cron_schedule="0 22 * * 0", job=implnet_job_cuahsi115, execution_timezone="US/Central")
def implnet_sch_cuahsi115(_context):
    run_config = {}
    return run_config
