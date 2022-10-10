from dagster import schedule

from jobs.implnet_jobs_name156 import implnet_job_name156

@schedule(cron_schedule="0 17 * * 0", job=implnet_job_name156, execution_timezone="US/Central")
def implnet_sch_name156(_context):
    run_config = {}
    return run_config
