from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_ref_princi_aq_princi_aq__0 import implnet_job_ref_princi_aq_princi_aq__0

@schedule(cron_schedule="0 18 25 * *", job=implnet_job_ref_princi_aq_princi_aq__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_ref_princi_aq_princi_aq__0(_context):
    run_config = {}
    return run_config
