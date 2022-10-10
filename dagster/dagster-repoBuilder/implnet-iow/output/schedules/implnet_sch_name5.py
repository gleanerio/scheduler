from dagster import schedule

from jobs.implnet_jobs_name5 import implnet_job_name5

@schedule(cron_schedule="0 4 * * 0", job=implnet_job_name5, execution_timezone="US/Central")
def implnet_sch_name5(_context):
    run_config = {}
    return run_config
