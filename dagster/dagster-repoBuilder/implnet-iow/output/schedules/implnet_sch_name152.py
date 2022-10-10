from dagster import schedule

from jobs.implnet_jobs_name152 import implnet_job_name152

@schedule(cron_schedule="0 13 * * 0", job=implnet_job_name152, execution_timezone="US/Central")
def implnet_sch_name152(_context):
    run_config = {}
    return run_config
