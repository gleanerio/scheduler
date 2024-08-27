from dagster import schedule

from jobs.implnet_jobs_nmwdiose4 import implnet_job_nmwdiose4

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_nmwdiose4, execution_timezone="US/Central")
def implnet_sch_nmwdiose4(_context):
    run_config = {}
    return run_config
