from dagster import schedule

from jobs.implnet_jobs_name174 import implnet_job_name174

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_name174, execution_timezone="US/Central")
def implnet_sch_name174(_context):
    run_config = {}
    return run_config
