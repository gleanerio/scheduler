from dagster import schedule

from jobs.implnet_jobs_ref55 import implnet_job_ref55

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_ref55, execution_timezone="US/Central")
def implnet_sch_ref55(_context):
    run_config = {}
    return run_config
