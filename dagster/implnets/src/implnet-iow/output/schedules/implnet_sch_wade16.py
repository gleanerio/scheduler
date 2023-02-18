from dagster import schedule

from jobs.implnet_jobs_wade16 import implnet_job_wade16

@schedule(cron_schedule="0 3 * * 1", job=implnet_job_wade16, execution_timezone="US/Central")
def implnet_sch_wade16(_context):
    run_config = {}
    return run_config
