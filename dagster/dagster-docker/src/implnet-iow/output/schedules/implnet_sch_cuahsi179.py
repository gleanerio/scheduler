from dagster import schedule

from jobs.implnet_jobs_cuahsi179 import implnet_job_cuahsi179

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi179, execution_timezone="US/Central")
def implnet_sch_cuahsi179(_context):
    run_config = {}
    return run_config
