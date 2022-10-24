from dagster import schedule

from jobs.implnet_jobs_selfie28 import implnet_job_selfie28

@schedule(cron_schedule="0 4 * * 0", job=implnet_job_selfie28, execution_timezone="US/Central")
def implnet_sch_selfie28(_context):
    run_config = {}
    return run_config
