from dagster import schedule

from jobs.implnet_jobs_wade20 import implnet_job_wade20

@schedule(cron_schedule="0 19 * * 0", job=implnet_job_wade20, execution_timezone="US/Central")
def implnet_sch_wade20(_context):
    run_config = {}
    return run_config