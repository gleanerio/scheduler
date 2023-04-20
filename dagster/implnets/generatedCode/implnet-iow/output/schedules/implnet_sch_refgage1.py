from dagster import schedule

from jobs.implnet_jobs_refgage1 import implnet_job_refgage1

@schedule(cron_schedule="0 18 * * 2", job=implnet_job_refgage1, execution_timezone="US/Central")
def implnet_sch_refgage1(_context):
    run_config = {}
    return run_config
