from dagster import schedule

from jobs.implnet_jobs_wade10 import implnet_job_wade10

@schedule(cron_schedule="0 4 2 * *", job=implnet_job_wade10, execution_timezone="US/Central")
def implnet_sch_wade10(_context):
    run_config = {}
    return run_config
