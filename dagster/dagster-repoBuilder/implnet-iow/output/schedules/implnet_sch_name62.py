from dagster import schedule

from jobs.implnet_jobs_name62 import implnet_job_name62

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_name62, execution_timezone="US/Central")
def implnet_sch_name62(_context):
    run_config = {}
    return run_config
