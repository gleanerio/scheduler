from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_usgs_monitoringlocation_nwisgw_nwisgw__24 import implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__24

@schedule(cron_schedule="0 0 23 * *", job=implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__24, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_usgs_monitoringlocation_nwisgw_nwisgw__24(_context):
    run_config = {}
    return run_config
