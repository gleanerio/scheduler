from dagster import schedule

from jobs.implnet_jobs_cuahsihiskansasweatherdataids0 import implnet_job_cuahsihiskansasweatherdataids0

@schedule(cron_schedule="0 0 10 * *", job=implnet_job_cuahsihiskansasweatherdataids0, execution_timezone="US/Central")
def implnet_sch_cuahsihiskansasweatherdataids0(_context):
    run_config = {}
    return run_config
