from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_usgs_monitoringlocation_nwissite_nwissite__1 import implnet_job_usgs_monitoringlocation_nwissite_nwissite__1

@schedule(cron_schedule="0 21 19 * *", job=implnet_job_usgs_monitoringlocation_nwissite_nwissite__1, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_usgs_monitoringlocation_nwissite_nwissite__1(_context):
    run_config = {}
    return run_config
