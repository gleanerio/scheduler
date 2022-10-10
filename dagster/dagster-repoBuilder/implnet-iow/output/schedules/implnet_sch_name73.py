from dagster import schedule

from jobs.implnet_jobs_name73 import implnet_job_name73

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_name73, execution_timezone="US/Central")
def implnet_sch_name73(_context):
    run_config = {}
    return run_config
