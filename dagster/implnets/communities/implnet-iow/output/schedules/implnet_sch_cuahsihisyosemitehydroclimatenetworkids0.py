from dagster import schedule

from jobs.implnet_jobs_cuahsihisyosemitehydroclimatenetworkids0 import implnet_job_cuahsihisyosemitehydroclimatenetworkids0

@schedule(cron_schedule="0 12 * * 5", job=implnet_job_cuahsihisyosemitehydroclimatenetworkids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisyosemitehydroclimatenetworkids0(_context):
    run_config = {}
    return run_config
