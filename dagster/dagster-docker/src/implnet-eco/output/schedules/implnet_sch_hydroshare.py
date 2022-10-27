from dagster import schedule

from jobs.implnet_jobs_hydroshare import implnet_job_hydroshare

@schedule(cron_schedule="0 12 * * 2", job=implnet_job_hydroshare, execution_timezone="US/Central")
def implnet_sch_hydroshare(_context):
    run_config = {}
    return run_config
