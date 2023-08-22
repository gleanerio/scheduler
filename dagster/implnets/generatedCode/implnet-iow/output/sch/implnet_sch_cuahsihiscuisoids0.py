from dagster import schedule

from jobs.implnet_jobs_cuahsihiscuisoids0 import implnet_job_cuahsihiscuisoids0

@schedule(cron_schedule="0 20 10 * *", job=implnet_job_cuahsihiscuisoids0, execution_timezone="US/Central")
def implnet_sch_cuahsihiscuisoids0(_context):
    run_config = {}
    return run_config
