from dagster import schedule

from jobs.implnet_jobs_name135 import implnet_job_name135

@schedule(cron_schedule="0 19 * * 0", job=implnet_job_name135, execution_timezone="US/Central")
def implnet_sch_name135(_context):
    run_config = {}
    return run_config
