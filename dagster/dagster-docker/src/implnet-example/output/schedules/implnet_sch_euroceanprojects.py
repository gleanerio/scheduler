from dagster import schedule

from jobs.implnet_jobs_euroceanprojects import implnet_job_euroceanprojects

@schedule(cron_schedule="0 12 * * 2", job=implnet_job_euroceanprojects, execution_timezone="US/Central")
def implnet_sch_euroceanprojects(_context):
    run_config = {}
    return run_config
