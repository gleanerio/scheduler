from dagster import schedule

from jobs.implnet_jobs_cuahsi108 import implnet_job_cuahsi108

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi108, execution_timezone="US/Central")
def implnet_sch_cuahsi108(_context):
    run_config = {}
    return run_config
