from dagster import schedule

from jobs.implnet_jobs_wade40 import implnet_job_wade40

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_wade40, execution_timezone="US/Central")
def implnet_sch_wade40(_context):
    run_config = {}
    return run_config
