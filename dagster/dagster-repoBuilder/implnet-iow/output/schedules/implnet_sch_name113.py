from dagster import schedule

from jobs.implnet_jobs_name113 import implnet_job_name113

@schedule(cron_schedule="0 20 * * 0", job=implnet_job_name113, execution_timezone="US/Central")
def implnet_sch_name113(_context):
    run_config = {}
    return run_config
