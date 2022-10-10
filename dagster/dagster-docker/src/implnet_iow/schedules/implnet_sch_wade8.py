from dagster import schedule

from jobs.implnet_jobs_wade8 import implnet_job_wade8

@schedule(cron_schedule="0 7 * * 0", job=implnet_job_wade8, execution_timezone="US/Central")
def implnet_sch_wade8(_context):
    run_config = {}
    return run_config
