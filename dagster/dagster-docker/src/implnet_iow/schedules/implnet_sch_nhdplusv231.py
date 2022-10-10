from dagster import schedule

from jobs.implnet_jobs_nhdplusv231 import implnet_job_nhdplusv231

@schedule(cron_schedule="0 7 * * 0", job=implnet_job_nhdplusv231, execution_timezone="US/Central")
def implnet_sch_nhdplusv231(_context):
    run_config = {}
    return run_config
