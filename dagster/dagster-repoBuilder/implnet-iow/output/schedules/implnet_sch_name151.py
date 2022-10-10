from dagster import schedule

from jobs.implnet_jobs_name151 import implnet_job_name151

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_name151, execution_timezone="US/Central")
def implnet_sch_name151(_context):
    run_config = {}
    return run_config
