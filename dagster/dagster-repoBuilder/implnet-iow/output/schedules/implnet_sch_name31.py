from dagster import schedule

from jobs.implnet_jobs_name31 import implnet_job_name31

@schedule(cron_schedule="0 7 * * 0", job=implnet_job_name31, execution_timezone="US/Central")
def implnet_sch_name31(_context):
    run_config = {}
    return run_config
