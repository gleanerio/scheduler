from dagster import schedule

from jobs.implnet_jobs_name25 import implnet_job_name25

@schedule(cron_schedule="0 1 * * 0", job=implnet_job_name25, execution_timezone="US/Central")
def implnet_sch_name25(_context):
    run_config = {}
    return run_config
