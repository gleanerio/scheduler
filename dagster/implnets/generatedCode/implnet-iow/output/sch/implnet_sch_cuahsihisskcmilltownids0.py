from dagster import schedule

from jobs.implnet_jobs_cuahsihisskcmilltownids0 import implnet_job_cuahsihisskcmilltownids0

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_cuahsihisskcmilltownids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisskcmilltownids0(_context):
    run_config = {}
    return run_config
