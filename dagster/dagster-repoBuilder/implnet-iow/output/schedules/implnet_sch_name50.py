from dagster import schedule

from jobs.implnet_jobs_name50 import implnet_job_name50

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_name50, execution_timezone="US/Central")
def implnet_sch_name50(_context):
    run_config = {}
    return run_config
