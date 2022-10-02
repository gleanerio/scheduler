from dagster import schedule

from gleaner.jobs.oih_jobs_oceanexperts import oih_job_oceanexperts

@schedule(cron_schedule="45 20 * * *", job=oih_job_oceanexperts, execution_timezone="US/Central")
def oih_sch_oceanexperts(_context):
    run_config = {}
    return run_config
