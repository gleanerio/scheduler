from dagster import schedule

from jobs.implnet_jobs_wade21 import implnet_job_wade21

@schedule(cron_schedule="0 20 * * 0", job=implnet_job_wade21, execution_timezone="US/Central")
def implnet_sch_wade21(_context):
    run_config = {}
    return run_config
