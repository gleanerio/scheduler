from dagster import schedule

from jobs.implnet_jobs_cuahsi152 import implnet_job_cuahsi152

@schedule(cron_schedule="0 13 * * 0", job=implnet_job_cuahsi152, execution_timezone="US/Central")
def implnet_sch_cuahsi152(_context):
    run_config = {}
    return run_config
