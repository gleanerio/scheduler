from dagster import schedule

from jobs.implnet_jobs_cuahsi170 import implnet_job_cuahsi170

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi170, execution_timezone="US/Central")
def implnet_sch_cuahsi170(_context):
    run_config = {}
    return run_config
