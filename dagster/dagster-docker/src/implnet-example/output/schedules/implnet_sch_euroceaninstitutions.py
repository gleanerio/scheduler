from dagster import schedule

from jobs.implnet_jobs_euroceaninstitutions import implnet_job_euroceaninstitutions

@schedule(cron_schedule="0 0 * * 2", job=implnet_job_euroceaninstitutions, execution_timezone="US/Central")
def implnet_sch_euroceaninstitutions(_context):
    run_config = {}
    return run_config
