from dagster import schedule

from jobs.implnet_jobs_inanodc import implnet_job_inanodc

@schedule(cron_schedule="0 12 * * 3", job=implnet_job_inanodc, execution_timezone="US/Central")
def implnet_sch_inanodc(_context):
    run_config = {}
    return run_config
