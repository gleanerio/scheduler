from dagster import schedule

from jobs.implnet_jobs_name7 import implnet_job_name7

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_name7, execution_timezone="US/Central")
def implnet_sch_name7(_context):
    run_config = {}
    return run_config
