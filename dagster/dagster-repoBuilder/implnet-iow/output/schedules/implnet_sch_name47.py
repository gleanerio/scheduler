from dagster import schedule

from jobs.implnet_jobs_name47 import implnet_job_name47

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_name47, execution_timezone="US/Central")
def implnet_sch_name47(_context):
    run_config = {}
    return run_config
