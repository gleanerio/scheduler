from dagster import schedule

from jobs.implnet_jobs_wardr import implnet_job_wardr

@schedule(cron_schedule="0 21 * * 0", job=implnet_job_wardr, execution_timezone="US/Central")
def implnet_sch_wardr(_context):
    run_config = {}
    return run_config
