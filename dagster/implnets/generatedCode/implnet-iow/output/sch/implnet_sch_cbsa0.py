from dagster import schedule

from jobs.implnet_jobs_cbsa0 import implnet_job_cbsa0

@schedule(cron_schedule="0 4 22 * *", job=implnet_job_cbsa0, execution_timezone="US/Central")
def implnet_sch_cbsa0(_context):
    run_config = {}
    return run_config
