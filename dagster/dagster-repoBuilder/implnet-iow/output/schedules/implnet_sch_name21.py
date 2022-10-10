from dagster import schedule

from jobs.implnet_jobs_name21 import implnet_job_name21

@schedule(cron_schedule="0 20 * * 0", job=implnet_job_name21, execution_timezone="US/Central")
def implnet_sch_name21(_context):
    run_config = {}
    return run_config
