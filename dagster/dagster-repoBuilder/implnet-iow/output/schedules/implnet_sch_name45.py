from dagster import schedule

from jobs.implnet_jobs_name45 import implnet_job_name45

@schedule(cron_schedule="0 21 * * 0", job=implnet_job_name45, execution_timezone="US/Central")
def implnet_sch_name45(_context):
    run_config = {}
    return run_config
