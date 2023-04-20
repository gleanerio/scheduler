from dagster import schedule

from jobs.implnet_jobs_ibict import implnet_job_ibict

@schedule(cron_schedule="0 21 * * 3", job=implnet_job_ibict, execution_timezone="US/Central")
def implnet_sch_ibict(_context):
    run_config = {}
    return run_config
