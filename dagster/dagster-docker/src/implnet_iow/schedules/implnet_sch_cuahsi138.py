from dagster import schedule

from jobs.implnet_jobs_cuahsi138 import implnet_job_cuahsi138

@schedule(cron_schedule="0 22 * * 0", job=implnet_job_cuahsi138, execution_timezone="US/Central")
def implnet_sch_cuahsi138(_context):
    run_config = {}
    return run_config
