from dagster import schedule

from jobs.implnet_jobs_cuahsi176 import implnet_job_cuahsi176

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi176, execution_timezone="US/Central")
def implnet_sch_cuahsi176(_context):
    run_config = {}
    return run_config
