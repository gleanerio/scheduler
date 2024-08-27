from dagster import schedule

from jobs.implnet_jobs_wade30 import implnet_job_wade30

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_wade30, execution_timezone="US/Central")
def implnet_sch_wade30(_context):
    run_config = {}
    return run_config
