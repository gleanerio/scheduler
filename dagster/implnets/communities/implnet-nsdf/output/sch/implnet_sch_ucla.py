from dagster import schedule

from jobs.implnet_jobs_ucla import implnet_job_ucla

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_ucla, execution_timezone="US/Central")
def implnet_sch_ucla(_context):
    run_config = {}
    return run_config
