from dagster import schedule

from jobs.implnet_jobs_ref45 import implnet_job_ref45

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_ref45, execution_timezone="US/Central")
def implnet_sch_ref45(_context):
    run_config = {}
    return run_config
