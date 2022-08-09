from dagster import schedule

from gleaner.jobs.oih_queue_maspawio import oih_queue_job_maspawio

@schedule(cron_schedule="0 6 * * *", job=oih_queue_job_maspawio, execution_timezone="US/Central")
def oih_queue_schedule_maspawio(_context):
    run_config = {}
    return run_config
