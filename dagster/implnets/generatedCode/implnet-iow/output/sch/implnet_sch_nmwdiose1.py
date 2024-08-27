from dagster import schedule

from jobs.implnet_jobs_nmwdiose1 import implnet_job_nmwdiose1

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_nmwdiose1, execution_timezone="US/Central")
def implnet_sch_nmwdiose1(_context):
    run_config = {}
    return run_config
