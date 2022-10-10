from dagster import schedule

from jobs.implnet_jobs_name115 import implnet_job_name115

@schedule(cron_schedule="0 22 * * 0", job=implnet_job_name115, execution_timezone="US/Central")
def implnet_sch_name115(_context):
    run_config = {}
    return run_config
