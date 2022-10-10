from dagster import schedule

from jobs.implnet_jobs_name80 import implnet_job_name80

@schedule(cron_schedule="0 10 * * 0", job=implnet_job_name80, execution_timezone="US/Central")
def implnet_sch_name80(_context):
    run_config = {}
    return run_config
