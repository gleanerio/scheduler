from dagster import schedule

from jobs.implnet_jobs_name105 import implnet_job_name105

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_name105, execution_timezone="US/Central")
def implnet_sch_name105(_context):
    run_config = {}
    return run_config
