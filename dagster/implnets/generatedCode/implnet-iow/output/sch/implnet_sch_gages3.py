from dagster import schedule

from jobs.implnet_jobs_gages3 import implnet_job_gages3

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_gages3, execution_timezone="US/Central")
def implnet_sch_gages3(_context):
    run_config = {}
    return run_config
