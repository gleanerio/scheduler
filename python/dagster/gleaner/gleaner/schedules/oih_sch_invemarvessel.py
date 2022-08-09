from dagster import schedule

from gleaner.jobs.oih_jobs_invemarvessel import oih_job_invemarvessel

@schedule(cron_schedule="30 20 * * *", job=oih_job_invemarvessel, execution_timezone="US/Central")
def oih_sch_invemarvessel(_context):
    run_config = {}
    return run_config
