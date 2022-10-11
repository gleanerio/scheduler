from dagster import schedule

from jobs.implnet_jobs_cuahsi116 import implnet_job_cuahsi116

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi116, execution_timezone="US/Central")
def implnet_sch_cuahsi116(_context):
    run_config = {}
    return run_config