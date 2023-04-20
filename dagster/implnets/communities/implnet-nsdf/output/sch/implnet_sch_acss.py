from dagster import schedule

from jobs.implnet_jobs_acss import implnet_job_acss

@schedule(cron_schedule="0 3 * * 1", job=implnet_job_acss, execution_timezone="US/Central")
def implnet_sch_acss(_context):
    run_config = {}
    return run_config
