from dagster import schedule

from jobs.implnet_jobs_name38 import implnet_job_name38

@schedule(cron_schedule="0 14 * * 0", job=implnet_job_name38, execution_timezone="US/Central")
def implnet_sch_name38(_context):
    run_config = {}
    return run_config
