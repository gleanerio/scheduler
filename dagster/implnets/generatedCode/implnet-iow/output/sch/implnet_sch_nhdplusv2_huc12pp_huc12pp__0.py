from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_nhdplusv2_huc12pp_huc12pp__0 import implnet_job_nhdplusv2_huc12pp_huc12pp__0

@schedule(cron_schedule="0 12 12 * *", job=implnet_job_nhdplusv2_huc12pp_huc12pp__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_nhdplusv2_huc12pp_huc12pp__0(_context):
    run_config = {}
    return run_config
