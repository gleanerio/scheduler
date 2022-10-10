from dagster import schedule

from jobs.implnet_jobs_name82 import implnet_job_name82

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_name82, execution_timezone="US/Central")
def implnet_sch_name82(_context):
    run_config = {}
    return run_config
