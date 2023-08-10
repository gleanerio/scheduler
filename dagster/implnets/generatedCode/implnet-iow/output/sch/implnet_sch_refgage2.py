from dagster import schedule

from jobs.implnet_jobs_refgage2 import implnet_job_refgage2

@schedule(cron_schedule="0 4 23 * *", job=implnet_job_refgage2, execution_timezone="US/Central")
def implnet_sch_refgage2(_context):
    run_config = {}
    return run_config
