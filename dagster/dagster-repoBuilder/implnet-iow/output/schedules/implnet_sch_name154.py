from dagster import schedule

from jobs.implnet_jobs_name154 import implnet_job_name154

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_name154, execution_timezone="US/Central")
def implnet_sch_name154(_context):
    run_config = {}
    return run_config
