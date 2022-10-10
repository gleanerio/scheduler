from dagster import schedule

from jobs.implnet_jobs_cuahsi162 import implnet_job_cuahsi162

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi162, execution_timezone="US/Central")
def implnet_sch_cuahsi162(_context):
    run_config = {}
    return run_config
