from dagster import schedule

from jobs.implnet_jobs_invemarexpert import implnet_job_invemarexpert

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_invemarexpert, execution_timezone="US/Central")
def implnet_sch_invemarexpert(_context):
    run_config = {}
    return run_config
