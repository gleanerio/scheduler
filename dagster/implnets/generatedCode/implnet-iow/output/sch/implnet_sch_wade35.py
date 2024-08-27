from dagster import schedule

from jobs.implnet_jobs_wade35 import implnet_job_wade35

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_wade35, execution_timezone="US/Central")
def implnet_sch_wade35(_context):
    run_config = {}
    return run_config
