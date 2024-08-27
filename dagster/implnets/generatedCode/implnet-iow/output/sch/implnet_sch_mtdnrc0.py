from dagster import schedule

from jobs.implnet_jobs_mtdnrc0 import implnet_job_mtdnrc0

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_mtdnrc0, execution_timezone="US/Central")
def implnet_sch_mtdnrc0(_context):
    run_config = {}
    return run_config
