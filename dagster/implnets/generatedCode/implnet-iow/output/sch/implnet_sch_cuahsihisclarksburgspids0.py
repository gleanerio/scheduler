from dagster import schedule

from jobs.implnet_jobs_cuahsihisclarksburgspids0 import implnet_job_cuahsihisclarksburgspids0

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_cuahsihisclarksburgspids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisclarksburgspids0(_context):
    run_config = {}
    return run_config
