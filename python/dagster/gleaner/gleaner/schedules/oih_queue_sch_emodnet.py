from dagster import schedule

from gleaner.jobs.oih_queue_emodnet import oih_queue_job_emodnet

@schedule(cron_schedule="0 4 * * *", job=oih_queue_job_emodnet, execution_timezone="US/Central")
def oih_queue_schedule_emodnet(_context):
    run_config = {}
    return run_config
