from dagster import schedule

from gleaner.jobs.oih_jobs_edmo import oih_job_edmo

@schedule(cron_schedule="0 18 * * *", job=oih_job_edmo, execution_timezone="US/Central")
def oih_sch_edmo(_context):
    run_config = {}
    return run_config
