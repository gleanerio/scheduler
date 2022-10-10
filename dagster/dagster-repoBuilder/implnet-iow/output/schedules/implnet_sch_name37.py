from dagster import schedule

from jobs.implnet_jobs_name37 import implnet_job_name37

@schedule(cron_schedule="0 13 * * 0", job=implnet_job_name37, execution_timezone="US/Central")
def implnet_sch_name37(_context):
    run_config = {}
    return run_config
