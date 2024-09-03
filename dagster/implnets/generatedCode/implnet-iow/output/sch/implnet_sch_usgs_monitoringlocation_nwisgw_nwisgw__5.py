from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_usgs_monitoringlocation_nwisgw_nwisgw__5 import implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__5

@schedule(cron_schedule="0 21 21 * *", job=implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__5, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_usgs_monitoringlocation_nwisgw_nwisgw__5(_context):
    run_config = {}
    return run_config
