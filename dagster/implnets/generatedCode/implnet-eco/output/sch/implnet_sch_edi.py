from dagster import schedule

from jobs.implnet_jobs_edi import implnet_job_edi

@schedule(cron_schedule="0 0 3 * *", job=implnet_job_edi, execution_timezone="US/Central")
def implnet_sch_edi(_context):
    run_config = {}
    return run_config
