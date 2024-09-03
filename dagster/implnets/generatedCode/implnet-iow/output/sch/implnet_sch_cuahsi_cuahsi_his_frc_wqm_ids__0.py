from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_cuahsi_cuahsi_his_frc_wqm_ids__0 import implnet_job_cuahsi_cuahsi_his_frc_wqm_ids__0

@schedule(cron_schedule="0 18 9 * *", job=implnet_job_cuahsi_cuahsi_his_frc_wqm_ids__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_cuahsi_cuahsi_his_frc_wqm_ids__0(_context):
    run_config = {}
    return run_config
