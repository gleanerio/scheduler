from dagster import schedule

from jobs.implnet_jobs_cuahsi168 import implnet_job_cuahsi168

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi168, execution_timezone="US/Central")
def implnet_sch_cuahsi168(_context):
    run_config = {}
    return run_config
