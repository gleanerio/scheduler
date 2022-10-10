from dagster import schedule

from jobs.implnet_jobs_name77 import implnet_job_name77

@schedule(cron_schedule="0 7 * * 0", job=implnet_job_name77, execution_timezone="US/Central")
def implnet_sch_name77(_context):
    run_config = {}
    return run_config
