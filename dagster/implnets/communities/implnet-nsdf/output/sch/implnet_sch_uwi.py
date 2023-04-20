from dagster import schedule

from jobs.implnet_jobs_uwi import implnet_job_uwi

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_uwi, execution_timezone="US/Central")
def implnet_sch_uwi(_context):
    run_config = {}
    return run_config
