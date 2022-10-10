from dagster import schedule

from jobs.implnet_jobs_name4 import implnet_job_name4

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_name4, execution_timezone="US/Central")
def implnet_sch_name4(_context):
    run_config = {}
    return run_config
