from dagster import schedule

from jobs.implnet_jobs_wade13 import implnet_job_wade13

@schedule(cron_schedule="0 16 2 * *", job=implnet_job_wade13, execution_timezone="US/Central")
def implnet_sch_wade13(_context):
    run_config = {}
    return run_config
