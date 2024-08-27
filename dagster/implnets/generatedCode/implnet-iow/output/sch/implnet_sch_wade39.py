from dagster import schedule

from jobs.implnet_jobs_wade39 import implnet_job_wade39

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_wade39, execution_timezone="US/Central")
def implnet_sch_wade39(_context):
    run_config = {}
    return run_config
