from dagster import schedule

from jobs.implnet_jobs_milano import implnet_job_milano

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_milano, execution_timezone="US/Central")
def implnet_sch_milano(_context):
    run_config = {}
    return run_config
