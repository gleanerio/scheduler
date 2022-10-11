from dagster import schedule

from jobs.implnet_jobs_wade5 import implnet_job_wade5

@schedule(cron_schedule="0 4 * * 0", job=implnet_job_wade5, execution_timezone="US/Central")
def implnet_sch_wade5(_context):
    run_config = {}
    return run_config