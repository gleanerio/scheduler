from dagster import schedule

from jobs.implnet_jobs_cuahsi164 import implnet_job_cuahsi164

@schedule(cron_schedule="0 2 * * 0", job=implnet_job_cuahsi164, execution_timezone="US/Central")
def implnet_sch_cuahsi164(_context):
    run_config = {}
    return run_config
