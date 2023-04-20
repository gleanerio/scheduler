from dagster import schedule

from jobs.implnet_jobs_aussda import implnet_job_aussda

@schedule(cron_schedule="0 12 * * 1", job=implnet_job_aussda, execution_timezone="US/Central")
def implnet_sch_aussda(_context):
    run_config = {}
    return run_config
