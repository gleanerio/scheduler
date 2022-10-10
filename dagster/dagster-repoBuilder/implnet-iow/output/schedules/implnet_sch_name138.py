from dagster import schedule

from jobs.implnet_jobs_name138 import implnet_job_name138

@schedule(cron_schedule="0 22 * * 0", job=implnet_job_name138, execution_timezone="US/Central")
def implnet_sch_name138(_context):
    run_config = {}
    return run_config
