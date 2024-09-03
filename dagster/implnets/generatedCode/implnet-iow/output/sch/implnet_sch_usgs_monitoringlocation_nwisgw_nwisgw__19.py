from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_usgs_monitoringlocation_nwisgw_nwisgw__19 import implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__19

@schedule(cron_schedule="0 0 22 * *", job=implnet_job_usgs_monitoringlocation_nwisgw_nwisgw__19, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_usgs_monitoringlocation_nwisgw_nwisgw__19(_context):
    run_config = {}
    return run_config
