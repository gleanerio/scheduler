from dagster import schedule

from jobs.implnet_jobs_nmwdi25 import implnet_job_nmwdi25

@schedule(cron_schedule="0 1 * * 0", job=implnet_job_nmwdi25, execution_timezone="US/Central")
def implnet_sch_nmwdi25(_context):
    run_config = {}
    return run_config
