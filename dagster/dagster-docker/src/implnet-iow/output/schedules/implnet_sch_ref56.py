from dagster import schedule

from jobs.implnet_jobs_ref56 import implnet_job_ref56

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_ref56, execution_timezone="US/Central")
def implnet_sch_ref56(_context):
    run_config = {}
    return run_config
