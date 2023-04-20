from dagster import schedule

from jobs.implnet_jobs_cimmyt import implnet_job_cimmyt

@schedule(cron_schedule="0 21 * * 1", job=implnet_job_cimmyt, execution_timezone="US/Central")
def implnet_sch_cimmyt(_context):
    run_config = {}
    return run_config
