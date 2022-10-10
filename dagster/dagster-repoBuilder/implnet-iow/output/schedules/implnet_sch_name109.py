from dagster import schedule

from jobs.implnet_jobs_name109 import implnet_job_name109

@schedule(cron_schedule="0 16 * * 0", job=implnet_job_name109, execution_timezone="US/Central")
def implnet_sch_name109(_context):
    run_config = {}
    return run_config
