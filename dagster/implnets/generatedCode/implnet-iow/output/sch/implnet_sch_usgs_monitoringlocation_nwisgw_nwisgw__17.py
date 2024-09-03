from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_usgs_monitoringlocation_nwisgw_nwisgw__17 import implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__17

@schedule(cron_schedule="0 15 20 * *", job=implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__17, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_usgs_monitoringlocation_nwisgw_nwisgw__17(_context):
    run_config = {}
    return run_config
