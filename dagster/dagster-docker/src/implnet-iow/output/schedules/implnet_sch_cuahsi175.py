from dagster import schedule

from jobs.implnet_jobs_cuahsi175 import implnet_job_cuahsi175

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi175, execution_timezone="US/Central")
def implnet_sch_cuahsi175(_context):
    run_config = {}
    return run_config
