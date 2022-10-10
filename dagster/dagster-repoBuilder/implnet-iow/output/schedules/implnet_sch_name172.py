from dagster import schedule

from jobs.implnet_jobs_name172 import implnet_job_name172

@schedule(cron_schedule="0 10 * * 0", job=implnet_job_name172, execution_timezone="US/Central")
def implnet_sch_name172(_context):
    run_config = {}
    return run_config
