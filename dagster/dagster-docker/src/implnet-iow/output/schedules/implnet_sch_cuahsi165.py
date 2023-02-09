from dagster import schedule

from jobs.implnet_jobs_cuahsi165 import implnet_job_cuahsi165

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi165, execution_timezone="US/Central")
def implnet_sch_cuahsi165(_context):
    run_config = {}
    return run_config
