from dagster import schedule

from jobs.implnet_jobs_cuahsihisccbepdapids0 import implnet_job_cuahsihisccbepdapids0

@schedule(cron_schedule="0 15 * * 6", job=implnet_job_cuahsihisccbepdapids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisccbepdapids0(_context):
    run_config = {}
    return run_config
