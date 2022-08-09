from dagster import schedule

from gleaner.jobs.oih_queue_pogo import oih_queue_job_pogo

@schedule(cron_schedule="0 8 * * *", job=oih_queue_job_pogo, execution_timezone="US/Central")
def oih_queue_schedule_pogo(_context):
    run_config = {}
    return run_config
