from dagster import schedule

from jobs.implnet_jobs_adf import implnet_job_adf

@schedule(cron_schedule="0 6 * * 1", job=implnet_job_adf, execution_timezone="US/Central")
def implnet_sch_adf(_context):
    run_config = {}
    return run_config
