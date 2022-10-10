from dagster import schedule

from jobs.implnet_jobs_name177 import implnet_job_name177

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_name177, execution_timezone="US/Central")
def implnet_sch_name177(_context):
    run_config = {}
    return run_config
