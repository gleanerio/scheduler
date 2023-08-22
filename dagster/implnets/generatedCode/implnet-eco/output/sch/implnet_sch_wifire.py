from dagster import schedule

from jobs.implnet_jobs_wifire import implnet_job_wifire

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_wifire, execution_timezone="US/Central")
def implnet_sch_wifire(_context):
    run_config = {}
    return run_config
