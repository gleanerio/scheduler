from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_cuahsi_cuahsi_his_shalenetworkodm_ids__1 import implnet_job_cuahsi_cuahsi_his_shalenetworkodm_ids__1

@schedule(cron_schedule="0 18 1 * *", job=implnet_job_cuahsi_cuahsi_his_shalenetworkodm_ids__1, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_cuahsi_cuahsi_his_shalenetworkodm_ids__1(_context):
    run_config = {}
    return run_config
