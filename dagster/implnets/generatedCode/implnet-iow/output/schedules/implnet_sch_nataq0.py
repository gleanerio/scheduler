from dagster import schedule

from jobs.implnet_jobs_nataq0 import implnet_job_nataq0

@schedule(cron_schedule="0 18 * * 1", job=implnet_job_nataq0, execution_timezone="US/Central")
def implnet_sch_nataq0(_context):
    run_config = {}
    return run_config
