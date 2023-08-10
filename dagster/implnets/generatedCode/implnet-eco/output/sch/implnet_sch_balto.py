from dagster import schedule

from jobs.implnet_jobs_balto import implnet_job_balto

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_balto, execution_timezone="US/Central")
def implnet_sch_balto(_context):
    run_config = {}
    return run_config
