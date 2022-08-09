from dagster import schedule

from gleaner.jobs.oih_queue_benguelacc import oih_queue_job_benguelacc

@schedule(cron_schedule="0 1 * * *", job=oih_queue_job_benguelacc, execution_timezone="US/Central")
def oih_queue_schedule_benguelacc(_context):
    run_config = {}
    return run_config
