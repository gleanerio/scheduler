from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_usgs_monitoringlocation_nwisgw_nwisgw__13 import implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__13

@schedule(cron_schedule="0 12 21 * *", job=implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__13, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_usgs_monitoringlocation_nwisgw_nwisgw__13(_context):
    run_config = {}
    return run_config
