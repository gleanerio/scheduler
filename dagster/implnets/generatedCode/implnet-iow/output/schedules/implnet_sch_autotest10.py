from dagster import schedule

from jobs.implnet_jobs_autotest10 import implnet_job_autotest10

@schedule(cron_schedule="0 15 * * 5", job=implnet_job_autotest10, execution_timezone="US/Central")
def implnet_sch_autotest10(_context):
    run_config = {}
    return run_config
