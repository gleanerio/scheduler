from dagster import schedule

from jobs.implnet_jobs_name110 import implnet_job_name110

@schedule(cron_schedule="0 17 * * 0", job=implnet_job_name110, execution_timezone="US/Central")
def implnet_sch_name110(_context):
    run_config = {}
    return run_config
