from dagster import schedule

from gleaner.jobs.oih_jobs_obps import oih_job_obps

@schedule(cron_schedule="30 3 * * *", job=oih_job_obps, execution_timezone="US/Central")
def oih_sch_obps(_context):
    run_config = {}
    return run_config
