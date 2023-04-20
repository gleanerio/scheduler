from dagster import schedule

from jobs.implnet_jobs_africaioc import implnet_job_africaioc

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_africaioc, execution_timezone="US/Central")
def implnet_sch_africaioc(_context):
    run_config = {}
    return run_config
