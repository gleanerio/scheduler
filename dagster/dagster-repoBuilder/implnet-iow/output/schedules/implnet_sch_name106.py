from dagster import schedule

from jobs.implnet_jobs_name106 import implnet_job_name106

@schedule(cron_schedule="0 13 * * 0", job=implnet_job_name106, execution_timezone="US/Central")
def implnet_sch_name106(_context):
    run_config = {}
    return run_config
