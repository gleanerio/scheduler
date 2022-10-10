from dagster import schedule

from jobs.implnet_jobs_name18 import implnet_job_name18

@schedule(cron_schedule="0 17 * * 0", job=implnet_job_name18, execution_timezone="US/Central")
def implnet_sch_name18(_context):
    run_config = {}
    return run_config
