from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_ref_sec_hydrg_reg_sec_hydrg_reg__0 import implnet_job_ref_sec_hydrg_reg_sec_hydrg_reg__0

@schedule(cron_schedule="0 12 25 * *", job=implnet_job_ref_sec_hydrg_reg_sec_hydrg_reg__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_ref_sec_hydrg_reg_sec_hydrg_reg__0(_context):
    run_config = {}
    return run_config
