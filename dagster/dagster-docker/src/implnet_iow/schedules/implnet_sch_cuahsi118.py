from dagster import schedule

from jobs.implnet_jobs_cuahsi118 import implnet_job_cuahsi118

@schedule(cron_schedule="0 2 * * 0", job=implnet_job_cuahsi118, execution_timezone="US/Central")
def implnet_sch_cuahsi118(_context):
    run_config = {}
    return run_config
