from dagster import schedule

from jobs.implnet_jobs_name9 import implnet_job_name9

@schedule(cron_schedule="0 8 * * 0", job=implnet_job_name9, execution_timezone="US/Central")
def implnet_sch_name9(_context):
    run_config = {}
    return run_config
