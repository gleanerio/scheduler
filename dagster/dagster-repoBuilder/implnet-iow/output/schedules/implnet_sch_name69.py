from dagster import schedule

from jobs.implnet_jobs_name69 import implnet_job_name69

@schedule(cron_schedule="0 22 * * 0", job=implnet_job_name69, execution_timezone="US/Central")
def implnet_sch_name69(_context):
    run_config = {}
    return run_config
