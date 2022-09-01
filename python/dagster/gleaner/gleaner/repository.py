from dagster import repository

from gleaner.jobs.oih_queue_benguelacc import oih_queue_job_benguelacc
from gleaner.jobs.oih_queue_cioos import oih_queue_job_cioos
from gleaner.jobs.oih_queue_cma import oih_queue_job_cma
from gleaner.jobs.oih_queue_emodnet import oih_queue_job_emodnet
from gleaner.jobs.oih_queue_inanodc import oih_queue_job_inanodc
from gleaner.jobs.oih_queue_maspawio import oih_queue_job_maspawio
from gleaner.jobs.oih_queue_pdh import oih_queue_job_pdh
from gleaner.jobs.oih_queue_pogo import oih_queue_job_pogo

from gleaner.jobs.oih_jobs_aquadocs import oih_job_aquadocs
from gleaner.jobs.oih_jobs_edmerp import oih_job_edmerp
from gleaner.jobs.oih_jobs_edmo import oih_job_edmo
from gleaner.jobs.oih_jobs_euroceanevents import oih_job_euroceanevents
from gleaner.jobs.oih_jobs_euroceanexpert import oih_job_euroceanexpert
from gleaner.jobs.oih_jobs_euroceanorgs import oih_job_euroceanorgs
from gleaner.jobs.oih_jobs_euroceanprojects import oih_job_euroceanprojects
from gleaner.jobs.oih_jobs_euroceantraining import oih_job_euroceantraining
from gleaner.jobs.oih_jobs_euroceanvessels import oih_job_euroceanvessels
from gleaner.jobs.oih_jobs_invemardocuments import oih_job_invemardocuments
from gleaner.jobs.oih_jobs_invemarexpert import oih_job_invemarexpert
from gleaner.jobs.oih_jobs_invemarinstitution import oih_job_invemarinstitution
from gleaner.jobs.oih_jobs_invemartraining import oih_job_invemartraining
from gleaner.jobs.oih_jobs_invemarvessel import oih_job_invemarvessel
from gleaner.jobs.oih_jobs_marinetraining import oih_job_marinetraining
from gleaner.jobs.oih_jobs_obis import oih_job_obis
from gleaner.jobs.oih_jobs_obps import oih_job_obps
from gleaner.jobs.oih_jobs_oceanexperts   import oih_job_oceanexperts

from gleaner.schedules.oih_queue_sch_benguelacc import oih_queue_schedule_benguelacc
from gleaner.schedules.oih_queue_sch_cioos import oih_queue_schedule_cioos
from gleaner.schedules.oih_queue_sch_cma import oih_queue_schedule_cma
from gleaner.schedules.oih_queue_sch_emodnet import oih_queue_schedule_emodnet
from gleaner.schedules.oih_queue_sch_inanodc import oih_queue_schedule_inanodc
from gleaner.schedules.oih_queue_sch_maspawio import oih_queue_schedule_maspawio
from gleaner.schedules.oih_queue_sch_pdh import oih_queue_schedule_pdh
from gleaner.schedules.oih_queue_sch_pogo import oih_queue_schedule_pogo

from gleaner.schedules.oih_sch_aquadocs import oih_sch_aquadocs
from gleaner.schedules.oih_sch_edmerp import oih_sch_edmerp
from gleaner.schedules.oih_sch_edmo import oih_sch_edmo
from gleaner.schedules.oih_sch_euroceanevents import oih_sch_euroceanevents
from gleaner.schedules.oih_sch_euroceanexpert import oih_sch_euroceanexpert
from gleaner.schedules.oih_sch_euroceanorgs import oih_sch_euroceanorgs
from gleaner.schedules.oih_sch_euroceanprojects import oih_sch_euroceanprojects
from gleaner.schedules.oih_sch_euroceantraining import oih_sch_euroceantraining
from gleaner.schedules.oih_sch_euroceanvessels import oih_sch_euroceanvessels
from gleaner.schedules.oih_sch_invemardocuments import oih_sch_invemardocuments
from gleaner.schedules.oih_sch_invemarexpert import oih_sch_invemarexpert
from gleaner.schedules.oih_sch_invemarinstitution import oih_sch_invemarinstitution
from gleaner.schedules.oih_sch_invemartraining import oih_sch_invemartraining
from gleaner.schedules.oih_sch_invemarvessel import oih_sch_invemarvessel
from gleaner.schedules.oih_sch_marinetraining import oih_sch_marinetraining
from gleaner.schedules.oih_sch_obis import oih_sch_obis
from gleaner.schedules.oih_sch_obps import oih_sch_obps
from gleaner.schedules.oih_sch_oceanexperts  import oih_sch_oceanexperts

# from gleaner.sensors.my_sensor import my_sensor


@repository
def gleaner():
    """
    The repository definition for this gleaner Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [oih_job_aquadocs, oih_job_edmerp, oih_job_edmo, oih_job_euroceanevents,
        oih_job_euroceanexpert, oih_job_euroceanorgs, oih_job_euroceanprojects,
        oih_job_euroceantraining, oih_job_euroceanvessels, oih_job_invemardocuments,
        oih_job_invemarexpert, oih_job_invemarinstitution, oih_job_invemartraining,
        oih_job_invemarvessel, oih_job_marinetraining, oih_job_obis, oih_job_obps,
        oih_job_oceanexperts, oih_queue_job_benguelacc, oih_queue_job_cioos, oih_queue_job_cma,
        oih_queue_job_emodnet, oih_queue_job_inanodc, oih_queue_job_maspawio,
        oih_queue_job_pdh, oih_queue_job_pogo]
    schedules = [oih_sch_aquadocs, oih_sch_edmerp, oih_sch_edmo, oih_sch_euroceanevents,
        oih_sch_euroceanexpert, oih_sch_euroceanorgs, oih_sch_euroceanprojects,
        oih_sch_euroceantraining, oih_sch_euroceanvessels, oih_sch_invemardocuments,
        oih_sch_invemarexpert, oih_sch_invemarinstitution, oih_sch_invemartraining,
        oih_sch_invemarvessel, oih_sch_marinetraining, oih_sch_obis, oih_sch_obps,
        oih_sch_oceanexperts, oih_queue_schedule_benguelacc, oih_queue_schedule_cioos,
        oih_queue_schedule_cma, oih_queue_schedule_emodnet, oih_queue_schedule_inanodc, oih_queue_schedule_maspawio, oih_queue_schedule_pdh, oih_queue_schedule_pogo]
    # sensors = [my_sensor]

    return jobs + schedules   #+ sensors
