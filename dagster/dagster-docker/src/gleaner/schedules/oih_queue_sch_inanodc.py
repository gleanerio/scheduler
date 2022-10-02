from dagster import schedule

from gleaner.jobs.oih_queue_inanodc import oih_queue_job_inanodc

@schedule(cron_schedule="0 5 * * *", job=oih_queue_job_inanodc, execution_timezone="US/Central")
def oih_queue_schedule_inanodc(_context):
    run_config = {}
    return run_config
