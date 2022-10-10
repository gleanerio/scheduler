from dagster import schedule

from jobs.implnet_jobs_name147 import implnet_job_name147

@schedule(cron_schedule="0 8 * * 0", job=implnet_job_name147, execution_timezone="US/Central")
def implnet_sch_name147(_context):
    run_config = {}
    return run_config
