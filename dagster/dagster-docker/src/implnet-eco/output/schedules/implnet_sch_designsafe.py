from dagster import schedule

from jobs.implnet_jobs_designsafe import implnet_job_designsafe

@schedule(cron_schedule="0 4 * * 0", job=implnet_job_designsafe, execution_timezone="US/Central")
def implnet_sch_designsafe(_context):
    run_config = {}
    return run_config
