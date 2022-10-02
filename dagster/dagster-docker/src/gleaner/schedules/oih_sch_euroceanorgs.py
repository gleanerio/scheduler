from dagster import schedule

from gleaner.jobs.oih_jobs_euroceanorgs import oih_job_euroceanorgs

@schedule(cron_schedule="0 21 * * *", job=oih_job_euroceanorgs, execution_timezone="US/Central")
def oih_sch_euroceanorgs(_context):
    run_config = {}
    return run_config
