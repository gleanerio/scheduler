from dagster import schedule

from jobs.implnet_jobs_ref54 import implnet_job_ref54

@schedule(cron_schedule="0 7 * * 0", job=implnet_job_ref54, execution_timezone="US/Central")
def implnet_sch_ref54(_context):
    run_config = {}
    return run_config
