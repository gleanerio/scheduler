from dagster import schedule

from jobs.implnet_jobs_cuahsi100 import implnet_job_cuahsi100

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi100, execution_timezone="US/Central")
def implnet_sch_cuahsi100(_context):
    run_config = {}
    return run_config
