from dagster import schedule

from jobs.implnet_jobs_cuahsihisgleonsunapeeids0 import implnet_job_cuahsihisgleonsunapeeids0

@schedule(cron_schedule="0 12 13 * *", job=implnet_job_cuahsihisgleonsunapeeids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisgleonsunapeeids0(_context):
    run_config = {}
    return run_config
