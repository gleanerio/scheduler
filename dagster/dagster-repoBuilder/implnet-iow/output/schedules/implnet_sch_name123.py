from dagster import schedule

from jobs.implnet_jobs_name123 import implnet_job_name123

@schedule(cron_schedule="0 7 * * 0", job=implnet_job_name123, execution_timezone="US/Central")
def implnet_sch_name123(_context):
    run_config = {}
    return run_config
