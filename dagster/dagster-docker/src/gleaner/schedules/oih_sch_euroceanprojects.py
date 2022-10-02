from dagster import schedule

from gleaner.jobs.oih_jobs_euroceanprojects import oih_job_euroceanprojects

@schedule(cron_schedule="0 22 * * *", job=oih_job_euroceanprojects, execution_timezone="US/Central")
def oih_sch_euroceanprojects(_context):
    run_config = {}
    return run_config
