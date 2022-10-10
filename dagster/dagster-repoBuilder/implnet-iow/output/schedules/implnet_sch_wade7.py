from dagster import schedule

from jobs.implnet_jobs_wade7 import implnet_job_wade7

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_wade7, execution_timezone="US/Central")
def implnet_sch_wade7(_context):
    run_config = {}
    return run_config
