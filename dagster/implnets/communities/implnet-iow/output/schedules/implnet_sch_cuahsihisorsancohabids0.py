from dagster import schedule

from jobs.implnet_jobs_cuahsihisorsancohabids0 import implnet_job_cuahsihisorsancohabids0

@schedule(cron_schedule="0 12 * * 2", job=implnet_job_cuahsihisorsancohabids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisorsancohabids0(_context):
    run_config = {}
    return run_config
