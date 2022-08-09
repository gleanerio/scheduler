from dagster import schedule

from gleaner.jobs.oih_jobs_marinetraining import oih_job_marinetraining

@schedule(cron_schedule="30 21 * * *", job=oih_job_marinetraining, execution_timezone="US/Central")
def oih_sch_marinetraining(_context):
    run_config = {}
    return run_config
