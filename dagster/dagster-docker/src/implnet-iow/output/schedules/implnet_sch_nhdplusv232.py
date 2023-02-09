from dagster import schedule

from jobs.implnet_jobs_nhdplusv232 import implnet_job_nhdplusv232

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_nhdplusv232, execution_timezone="US/Central")
def implnet_sch_nhdplusv232(_context):
    run_config = {}
    return run_config
