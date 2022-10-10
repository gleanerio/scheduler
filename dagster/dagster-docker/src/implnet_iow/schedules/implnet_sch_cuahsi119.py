from dagster import schedule

from jobs.implnet_jobs_cuahsi119 import implnet_job_cuahsi119

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_cuahsi119, execution_timezone="US/Central")
def implnet_sch_cuahsi119(_context):
    run_config = {}
    return run_config
