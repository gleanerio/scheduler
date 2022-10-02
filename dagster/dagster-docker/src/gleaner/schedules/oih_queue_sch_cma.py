from dagster import schedule

from gleaner.jobs.oih_queue_cma import oih_queue_job_cma

@schedule(cron_schedule="0 3 * * *", job=oih_queue_job_cma, execution_timezone="US/Central")
def oih_queue_schedule_cma(_context):
    run_config = {}
    return run_config
