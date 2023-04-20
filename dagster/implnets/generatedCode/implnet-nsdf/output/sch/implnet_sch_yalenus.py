from dagster import schedule

from jobs.implnet_jobs_yalenus import implnet_job_yalenus

@schedule(cron_schedule="0 0 * * 1", job=implnet_job_yalenus, execution_timezone="US/Central")
def implnet_sch_yalenus(_context):
    run_config = {}
    return run_config
