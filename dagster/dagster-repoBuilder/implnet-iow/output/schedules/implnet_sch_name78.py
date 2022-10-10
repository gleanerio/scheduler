from dagster import schedule

from jobs.implnet_jobs_name78 import implnet_job_name78

@schedule(cron_schedule="0 8 * * 0", job=implnet_job_name78, execution_timezone="US/Central")
def implnet_sch_name78(_context):
    run_config = {}
    return run_config
