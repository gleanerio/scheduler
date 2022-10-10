from dagster import schedule

from jobs.implnet_jobs_name171 import implnet_job_name171

@schedule(cron_schedule="0 9 * * 0", job=implnet_job_name171, execution_timezone="US/Central")
def implnet_sch_name171(_context):
    run_config = {}
    return run_config
