from dagster import schedule

from jobs.implnet_jobs_name142 import implnet_job_name142

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_name142, execution_timezone="US/Central")
def implnet_sch_name142(_context):
    run_config = {}
    return run_config
