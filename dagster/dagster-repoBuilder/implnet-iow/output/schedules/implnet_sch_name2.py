from dagster import schedule

from jobs.implnet_jobs_name2 import implnet_job_name2

@schedule(cron_schedule="0 1 * * 0", job=implnet_job_name2, execution_timezone="US/Central")
def implnet_sch_name2(_context):
    run_config = {}
    return run_config
