from dagster import schedule

from jobs.implnet_jobs_hord import implnet_job_hord

@schedule(cron_schedule="0 18 * * 3", job=implnet_job_hord, execution_timezone="US/Central")
def implnet_sch_hord(_context):
    run_config = {}
    return run_config
