from dagster import schedule

from gleaner.jobs.oih_queue_pdh import oih_queue_job_pdh

@schedule(cron_schedule="0 7 * * *", job=oih_queue_job_pdh, execution_timezone="US/Central")
def oih_queue_schedule_pdh(_context):
    run_config = {}
    return run_config
