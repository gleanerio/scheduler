from dagster import schedule

from gleaner.jobs.oih_jobs_euroceanexpert import oih_job_euroceanexpert

@schedule(cron_schedule="0 20 * * *", job=oih_job_euroceanexpert, execution_timezone="US/Central")
def oih_sch_euroceanexpert(_context):
    run_config = {}
    return run_config
