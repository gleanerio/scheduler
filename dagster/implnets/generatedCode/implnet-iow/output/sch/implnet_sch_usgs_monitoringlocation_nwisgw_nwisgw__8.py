from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_usgs_monitoringlocation_nwisgw_nwisgw__8 import implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__8

@schedule(cron_schedule="0 3 22 * *", job=implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__8, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_usgs_monitoringlocation_nwisgw_nwisgw__8(_context):
    run_config = {}
    return run_config
