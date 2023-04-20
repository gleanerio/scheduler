from dagster import schedule

from jobs.implnet_jobs_ucdl import implnet_job_ucdl

@schedule(cron_schedule="0 18 * * 5", job=implnet_job_ucdl, execution_timezone="US/Central")
def implnet_sch_ucdl(_context):
    run_config = {}
    return run_config
