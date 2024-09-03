from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_nmwdi_ose_nmwdiose__4 import implnet_job_nmwdi_ose_nmwdiose__4

@schedule(cron_schedule="0 3 12 * *", job=implnet_job_nmwdi_ose_nmwdiose__4, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_nmwdi_ose_nmwdiose__4(_context):
    run_config = {}
    return run_config
