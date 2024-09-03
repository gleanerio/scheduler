from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_nmwdi_st_nmwdist__0 import implnet_job_nmwdi_st_nmwdist__0

@schedule(cron_schedule="0 15 11 * *", job=implnet_job_nmwdi_st_nmwdist__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_nmwdi_st_nmwdist__0(_context):
    run_config = {}
    return run_config
