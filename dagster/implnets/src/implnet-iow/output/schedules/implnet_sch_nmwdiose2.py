from dagster import schedule

from jobs.implnet_jobs_nmwdiose2 import implnet_job_nmwdiose2

@schedule(cron_schedule="0 15 * * 4", job=implnet_job_nmwdiose2, execution_timezone="US/Central")
def implnet_sch_nmwdiose2(_context):
    run_config = {}
    return run_config
