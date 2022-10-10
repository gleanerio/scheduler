from dagster import schedule

from jobs.implnet_jobs_name130 import implnet_job_name130

@schedule(cron_schedule="0 14 * * 0", job=implnet_job_name130, execution_timezone="US/Central")
def implnet_sch_name130(_context):
    run_config = {}
    return run_config
