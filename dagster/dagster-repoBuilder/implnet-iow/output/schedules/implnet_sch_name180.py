from dagster import schedule

from jobs.implnet_jobs_name180 import implnet_job_name180

@schedule(cron_schedule="0 18 * * 0", job=implnet_job_name180, execution_timezone="US/Central")
def implnet_sch_name180(_context):
    run_config = {}
    return run_config
