from dagster import schedule

from gleaner.jobs.oih_jobs_aquadocs import oih_job_aquadocs

@schedule(cron_schedule="0 16 * * *", job=oih_job_aquadocs, execution_timezone="US/Central")
def oih_sch_aquadocs(_context):
    run_config = {}
    return run_config
