from dagster import schedule

from jobs.implnet_jobs_iris import implnet_job_iris

@schedule(cron_schedule="0 8 4 * *", job=implnet_job_iris, execution_timezone="US/Central")
def implnet_sch_iris(_context):
    run_config = {}
    return run_config
