from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_cagageassessment_ca_gages_pids__0 import implnet_job_cagageassessment_ca_gages_pids__0

@schedule(cron_schedule="0 21 27 * *", job=implnet_job_cagageassessment_ca_gages_pids__0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_cagageassessment_ca_gages_pids__0(_context):
    run_config = {}
    return run_config
