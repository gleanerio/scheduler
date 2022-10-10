from dagster import schedule

from jobs.implnet_jobs_name122 import implnet_job_name122

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_name122, execution_timezone="US/Central")
def implnet_sch_name122(_context):
    run_config = {}
    return run_config
