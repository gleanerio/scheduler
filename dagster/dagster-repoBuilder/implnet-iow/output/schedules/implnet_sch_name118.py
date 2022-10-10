from dagster import schedule

from jobs.implnet_jobs_name118 import implnet_job_name118

@schedule(cron_schedule="0 2 * * 0", job=implnet_job_name118, execution_timezone="US/Central")
def implnet_sch_name118(_context):
    run_config = {}
    return run_config
