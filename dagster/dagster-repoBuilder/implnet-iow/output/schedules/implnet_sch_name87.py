from dagster import schedule

from jobs.implnet_jobs_name87 import implnet_job_name87

@schedule(cron_schedule="0 17 * * 0", job=implnet_job_name87, execution_timezone="US/Central")
def implnet_sch_name87(_context):
    run_config = {}
    return run_config
