from dagster import schedule

from gleaner.jobs.oih_jobs_obis import oih_job_obis

@schedule(cron_schedule="30 22 * * 5", job=oih_job_obis, execution_timezone="US/Central")
def oih_sch_obis(_context):
    run_config = {}
    return run_config
