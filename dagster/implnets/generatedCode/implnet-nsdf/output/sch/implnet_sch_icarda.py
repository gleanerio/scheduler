from dagster import schedule

from jobs.implnet_jobs_icarda import implnet_job_icarda

@schedule(cron_schedule="0 12 * * 5", job=implnet_job_icarda, execution_timezone="US/Central")
def implnet_sch_icarda(_context):
    run_config = {}
    return run_config
