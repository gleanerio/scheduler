from dagster import schedule

from jobs.implnet_jobs_pdh import implnet_job_pdh

@schedule(cron_schedule="0 12 * * 6", job=implnet_job_pdh, execution_timezone="US/Central")
def implnet_sch_pdh(_context):
    run_config = {}
    return run_config
