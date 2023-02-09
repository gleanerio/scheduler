from dagster import schedule

from jobs.implnet_jobs_cuahsi102 import implnet_job_cuahsi102

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi102, execution_timezone="US/Central")
def implnet_sch_cuahsi102(_context):
    run_config = {}
    return run_config
