from dagster import schedule

from jobs.implnet_jobs_wade44 import implnet_job_wade44

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_wade44, execution_timezone="US/Central")
def implnet_sch_wade44(_context):
    run_config = {}
    return run_config
