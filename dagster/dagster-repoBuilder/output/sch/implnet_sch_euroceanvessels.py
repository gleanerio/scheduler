from dagster import schedule

from gleaner.jobs.implnet_jobs_euroceanvessels import implnet_job_euroceanvessels

@schedule(cron_schedule="0 16 * * *", job=implnet_job_euroceanvessels, execution_timezone="US/Central")
def implnet_sch_euroceanvessels(_context):
    run_config = {}
    return run_config
