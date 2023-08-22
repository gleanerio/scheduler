from dagster import schedule

from jobs.implnet_jobs_cuahsihisfrcwqmids0 import implnet_job_cuahsihisfrcwqmids0

@schedule(cron_schedule="0 8 17 * *", job=implnet_job_cuahsihisfrcwqmids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisfrcwqmids0(_context):
    run_config = {}
    return run_config
