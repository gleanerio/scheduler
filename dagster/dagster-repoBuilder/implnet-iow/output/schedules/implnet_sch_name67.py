from dagster import schedule

from jobs.implnet_jobs_name67 import implnet_job_name67

@schedule(cron_schedule="0 20 * * 0", job=implnet_job_name67, execution_timezone="US/Central")
def implnet_sch_name67(_context):
    run_config = {}
    return run_config
