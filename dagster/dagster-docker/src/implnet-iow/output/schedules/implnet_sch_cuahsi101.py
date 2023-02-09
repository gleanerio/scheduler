from dagster import schedule

from jobs.implnet_jobs_cuahsi101 import implnet_job_cuahsi101

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi101, execution_timezone="US/Central")
def implnet_sch_cuahsi101(_context):
    run_config = {}
    return run_config
