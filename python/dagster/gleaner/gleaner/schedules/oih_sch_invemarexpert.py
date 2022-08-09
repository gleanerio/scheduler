from dagster import schedule

from gleaner.jobs.oih_jobs_invemarexpert import oih_job_invemarexpert

@schedule(cron_schedule="20 17 * * *", job=oih_job_invemarexpert, execution_timezone="US/Central")
def oih_sch_invemarexpert(_context):
    run_config = {}
    return run_config
