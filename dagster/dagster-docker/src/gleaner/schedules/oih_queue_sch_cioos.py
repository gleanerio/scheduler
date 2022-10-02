from dagster import schedule

from gleaner.jobs.oih_queue_cioos import oih_queue_job_cioos

@schedule(cron_schedule="0 2 * * *", job=oih_queue_job_cioos, execution_timezone="US/Central")
def oih_queue_schedule_cioos(_context):
    run_config = {}
    return run_config
