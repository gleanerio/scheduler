from dagster import schedule

from gleaner.jobs.oih_queue import oih_queue_job


@schedule(cron_schedule="0 7 * * *", job=oih_queue_job, execution_timezone="US/Central")
def oih_queue_schedule(_context):
    """
    A schedule definition. This example schedule runs once each hour.

    For more hints on running jobs with schedules in Dagster, see our documentation overview on
    schedules:
    https://docs.dagster.io/overview/schedules-sensors/schedules
    """
    run_config = {}
    return run_config
