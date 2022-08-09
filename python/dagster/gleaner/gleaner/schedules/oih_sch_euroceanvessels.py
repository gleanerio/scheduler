from dagster import schedule

from gleaner.jobs.oih_jobs_euroceanvessels import oih_job_euroceanvessels

@schedule(cron_schedule="30 23 * * *", job=oih_job_euroceanvessels, execution_timezone="US/Central")
def oih_sch_euroceanvessels(_context):
    run_config = {}
    return run_config
