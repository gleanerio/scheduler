from dagster import schedule

from jobs.implnet_jobs_demo0 import implnet_job_demo0

@schedule(cron_schedule="0 12 27 * *", job=implnet_job_demo0, execution_timezone="US/Central")
def implnet_sch_demo0(_context):
    run_config = {}
    return run_config
