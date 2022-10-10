from dagster import schedule

from jobs.implnet_jobs_name42 import implnet_job_name42

@schedule(cron_schedule="0 18 * * 0", job=implnet_job_name42, execution_timezone="US/Central")
def implnet_sch_name42(_context):
    run_config = {}
    return run_config
