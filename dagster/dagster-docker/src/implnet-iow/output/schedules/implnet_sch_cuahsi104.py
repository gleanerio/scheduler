from dagster import schedule

from jobs.implnet_jobs_cuahsi104 import implnet_job_cuahsi104

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi104, execution_timezone="US/Central")
def implnet_sch_cuahsi104(_context):
    run_config = {}
    return run_config
