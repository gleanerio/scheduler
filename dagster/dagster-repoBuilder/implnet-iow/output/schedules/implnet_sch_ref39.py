from dagster import schedule

from jobs.implnet_jobs_ref39 import implnet_job_ref39

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_ref39, execution_timezone="US/Central")
def implnet_sch_ref39(_context):
    run_config = {}
    return run_config
