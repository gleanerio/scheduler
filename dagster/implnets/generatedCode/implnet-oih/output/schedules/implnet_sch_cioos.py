from dagster import schedule

from jobs.implnet_jobs_cioos import implnet_job_cioos

@schedule(cron_schedule="0 0 * * 1", job=implnet_job_cioos, execution_timezone="US/Central")
def implnet_sch_cioos(_context):
    run_config = {}
    return run_config
