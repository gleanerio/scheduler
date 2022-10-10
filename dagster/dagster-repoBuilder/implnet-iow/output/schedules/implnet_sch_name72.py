from dagster import schedule

from jobs.implnet_jobs_name72 import implnet_job_name72

@schedule(cron_schedule="0 2 * * 0", job=implnet_job_name72, execution_timezone="US/Central")
def implnet_sch_name72(_context):
    run_config = {}
    return run_config
