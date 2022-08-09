from dagster import schedule

from gleaner.jobs.oih_jobs_invemardocuments import oih_job_invemardocuments

@schedule(cron_schedule="30 16 * * *", job=oih_job_invemardocuments, execution_timezone="US/Central")
def oih_sch_invemardocuments(_context):
    run_config = {}
    return run_config
