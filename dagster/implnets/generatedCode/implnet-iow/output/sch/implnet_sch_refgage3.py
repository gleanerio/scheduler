from dagster import schedule

from jobs.implnet_jobs_refgage3 import implnet_job_refgage3

@schedule(cron_schedule="0 0 23 * *", job=implnet_job_refgage3, execution_timezone="US/Central")
def implnet_sch_refgage3(_context):
    run_config = {}
    return run_config
