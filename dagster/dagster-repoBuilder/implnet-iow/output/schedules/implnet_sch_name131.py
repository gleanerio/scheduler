from dagster import schedule

from jobs.implnet_jobs_name131 import implnet_job_name131

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_name131, execution_timezone="US/Central")
def implnet_sch_name131(_context):
    run_config = {}
    return run_config
