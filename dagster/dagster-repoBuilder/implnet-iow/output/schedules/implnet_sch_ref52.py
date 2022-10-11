from dagster import schedule

from jobs.implnet_jobs_ref52 import implnet_job_ref52

@schedule(cron_schedule="0 5 * * 0", job=implnet_job_ref52, execution_timezone="US/Central")
def implnet_sch_ref52(_context):
    run_config = {}
    return run_config