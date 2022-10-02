from dagster import schedule

from gleaner.jobs.oih_jobs_edmerp import oih_job_edmerp

@schedule(cron_schedule="0 17 * * *", job=oih_job_edmerp, execution_timezone="US/Central")
def oih_sch_edmerp(_context):
    run_config = {}
    return run_config
