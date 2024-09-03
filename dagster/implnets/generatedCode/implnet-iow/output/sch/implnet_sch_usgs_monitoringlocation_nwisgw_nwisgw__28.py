from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_usgs_monitoringlocation_nwisgw_nwisgw__28 import implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__28

@schedule(cron_schedule="0 3 21 * *", job=implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__28, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_usgs_monitoringlocation_nwisgw_nwisgw__28(_context):
    run_config = {}
    return run_config
