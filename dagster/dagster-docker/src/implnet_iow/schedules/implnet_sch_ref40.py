from dagster import schedule

from jobs.implnet_jobs_ref40 import implnet_job_ref40

@schedule(cron_schedule="0 16 * * 0", job=implnet_job_ref40, execution_timezone="US/Central")
def implnet_sch_ref40(_context):
    run_config = {}
    return run_config
