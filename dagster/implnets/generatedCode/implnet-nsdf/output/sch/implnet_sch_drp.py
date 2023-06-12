from dagster import schedule

from jobs.implnet_jobs_drp import implnet_job_drp

@schedule(cron_schedule="0 9 * * 0", job=implnet_job_drp, execution_timezone="US/Central")
def implnet_sch_drp(_context):
    run_config = {}
    return run_config
