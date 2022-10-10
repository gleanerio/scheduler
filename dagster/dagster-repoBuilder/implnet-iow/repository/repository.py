from dagster import repository

from gleaner.jobs.implnet_jobs_SOURCEVAL import implnet_job_SOURCEVAL
from gleaner.schedules.implnet_sch_SOURCEVAL  import implnet_sch_SOURCEVAL
# from gleaner.sensors.my_sensor import my_sensor

@repository
def gleaner():
    jobs = [implnet_job_SOURCEVAL]
    schedules = [implnet_sch_SOURCEVAL]
    # sensors = [my_sensor]

    return jobs + schedules   #+ sensors
