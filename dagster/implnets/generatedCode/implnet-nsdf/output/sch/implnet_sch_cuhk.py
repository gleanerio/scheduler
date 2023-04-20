from dagster import schedule

from jobs.implnet_jobs_cuhk import implnet_job_cuhk

@schedule(cron_schedule="0 6 * * 2", job=implnet_job_cuhk, execution_timezone="US/Central")
def implnet_sch_cuhk(_context):
    run_config = {}
    return run_config
