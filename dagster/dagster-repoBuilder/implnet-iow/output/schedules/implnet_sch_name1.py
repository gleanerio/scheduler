from dagster import schedule

from jobs.implnet_jobs_name1 import implnet_job_name1

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_name1, execution_timezone="US/Central")
def implnet_sch_name1(_context):
    run_config = {}
    return run_config
