from dagster import schedule

from jobs.implnet_jobs_name90 import implnet_job_name90

@schedule(cron_schedule="0 20 * * 0", job=implnet_job_name90, execution_timezone="US/Central")
def implnet_sch_name90(_context):
    run_config = {}
    return run_config
