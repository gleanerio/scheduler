from dagster import schedule

from jobs.implnet_jobs_name71 import implnet_job_name71

@schedule(cron_schedule="0 1 * * 0", job=implnet_job_name71, execution_timezone="US/Central")
def implnet_sch_name71(_context):
    run_config = {}
    return run_config
