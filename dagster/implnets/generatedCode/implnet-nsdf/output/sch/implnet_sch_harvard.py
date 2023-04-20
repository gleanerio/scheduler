from dagster import schedule

from jobs.implnet_jobs_harvard import implnet_job_harvard

@schedule(cron_schedule="0 15 * * 3", job=implnet_job_harvard, execution_timezone="US/Central")
def implnet_sch_harvard(_context):
    run_config = {}
    return run_config
