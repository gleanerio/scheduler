from dagster import schedule

from jobs.implnet_jobs_cuahsi128 import implnet_job_cuahsi128

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi128, execution_timezone="US/Central")
def implnet_sch_cuahsi128(_context):
    run_config = {}
    return run_config
