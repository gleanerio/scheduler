from dagster import schedule

from gleaner.jobs.implnet_jobs_euroceanorgs import implnet_job_euroceanorgs

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_euroceanorgs, execution_timezone="US/Central")
def implnet_sch_euroceanorgs(_context):
    run_config = {}
    return run_config
