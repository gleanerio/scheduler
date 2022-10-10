from dagster import schedule

from jobs.implnet_jobs_name149 import implnet_job_name149

@schedule(cron_schedule="0 10 * * 0", job=implnet_job_name149, execution_timezone="US/Central")
def implnet_sch_name149(_context):
    run_config = {}
    return run_config
