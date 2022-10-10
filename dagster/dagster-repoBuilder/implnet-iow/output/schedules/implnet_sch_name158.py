from dagster import schedule

from jobs.implnet_jobs_name158 import implnet_job_name158

@schedule(cron_schedule="0 19 * * 0", job=implnet_job_name158, execution_timezone="US/Central")
def implnet_sch_name158(_context):
    run_config = {}
    return run_config
