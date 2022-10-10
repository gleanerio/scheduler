from dagster import schedule

from jobs.implnet_jobs_name14 import implnet_job_name14

@schedule(cron_schedule="0 13 * * 0", job=implnet_job_name14, execution_timezone="US/Central")
def implnet_sch_name14(_context):
    run_config = {}
    return run_config
