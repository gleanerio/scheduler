from dagster import schedule

from jobs.implnet_jobs_nmwdiose3 import implnet_job_nmwdiose3

@schedule(cron_schedule="0 16 25 * *", job=implnet_job_nmwdiose3, execution_timezone="US/Central")
def implnet_sch_nmwdiose3(_context):
    run_config = {}
    return run_config
