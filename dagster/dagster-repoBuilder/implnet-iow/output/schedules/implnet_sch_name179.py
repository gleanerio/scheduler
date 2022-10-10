from dagster import schedule

from jobs.implnet_jobs_name179 import implnet_job_name179

@schedule(cron_schedule="0 17 * * 0", job=implnet_job_name179, execution_timezone="US/Central")
def implnet_sch_name179(_context):
    run_config = {}
    return run_config
