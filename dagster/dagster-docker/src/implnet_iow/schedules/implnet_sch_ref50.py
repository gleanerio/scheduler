from dagster import schedule

from jobs.implnet_jobs_ref50 import implnet_job_ref50

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_ref50, execution_timezone="US/Central")
def implnet_sch_ref50(_context):
    run_config = {}
    return run_config
