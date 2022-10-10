from dagster import schedule

from jobs.implnet_jobs_ref44 import implnet_job_ref44

@schedule(cron_schedule="0 20 * * 0", job=implnet_job_ref44, execution_timezone="US/Central")
def implnet_sch_ref44(_context):
    run_config = {}
    return run_config
