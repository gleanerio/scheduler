from dagster import schedule

from jobs.implnet_jobs_euroceanevents import implnet_job_euroceanevents

@schedule(cron_schedule="0 12 * * 1", job=implnet_job_euroceanevents, execution_timezone="US/Central")
def implnet_sch_euroceanevents(_context):
    run_config = {}
    return run_config
