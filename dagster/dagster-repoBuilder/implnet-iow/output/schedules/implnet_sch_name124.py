from dagster import schedule

from jobs.implnet_jobs_name124 import implnet_job_name124

@schedule(cron_schedule="0 8 * * 0", job=implnet_job_name124, execution_timezone="US/Central")
def implnet_sch_name124(_context):
    run_config = {}
    return run_config
