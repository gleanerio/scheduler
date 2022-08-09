from dagster import schedule

from gleaner.jobs.oih_jobs_euroceanevents import oih_job_euroceanevents

@schedule(cron_schedule="0 19 * * *", job=oih_job_euroceanevents, execution_timezone="US/Central")
def oih_sch_euroceanevents(_context):
    run_config = {}
    return run_config
