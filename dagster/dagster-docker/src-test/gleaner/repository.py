from dagster import repository

from gleaner.jobs.oih_jobs_aquadocs import oih_job_aquadocs
from gleaner.schedules.oih_sch_aquadocs import oih_sch_aquadocs

@repository
def gleaner():
    jobs = [oih_job_aquadocs]
    schedules = [oih_sch_aquadocs]

    return jobs + schedules   #+ sensors
