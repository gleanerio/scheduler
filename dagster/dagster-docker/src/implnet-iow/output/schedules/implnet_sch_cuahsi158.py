from dagster import schedule

from jobs.implnet_jobs_cuahsi158 import implnet_job_cuahsi158

@schedule(cron_schedule="0 19 * * 0", job=implnet_job_cuahsi158, execution_timezone="US/Central")
def implnet_sch_cuahsi158(_context):
    run_config = {}
    return run_config
