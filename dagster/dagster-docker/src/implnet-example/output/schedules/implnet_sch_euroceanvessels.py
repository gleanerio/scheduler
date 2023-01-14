from dagster import schedule

from jobs.implnet_jobs_euroceanvessels import implnet_job_euroceanvessels

@schedule(cron_schedule="0 0 * * 3", job=implnet_job_euroceanvessels, execution_timezone="US/Central")
def implnet_sch_euroceanvessels(_context):
    run_config = {}
    return run_config
