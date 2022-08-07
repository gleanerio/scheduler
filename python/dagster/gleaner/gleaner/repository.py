from dagster import repository

from gleaner.jobs.say_hello import say_hello_job
from gleaner.jobs.oih_queue import oih_queue_job
from gleaner.schedules.my_hourly_schedule import my_hourly_schedule
from gleaner.schedules.oih_queue_schedule import oih_queue_schedule
from gleaner.sensors.my_sensor import my_sensor


@repository
def gleaner():
    """
    The repository definition for this gleaner Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [say_hello_job,oih_queue_job]
    schedules = [my_hourly_schedule,oih_queue_schedule]
    sensors = [my_sensor]

    return jobs + schedules + sensors
