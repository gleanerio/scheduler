from dagster import schedule

from jobs.implnet_jobs_cuahsihisirwaids0 import implnet_job_cuahsihisirwaids0

@schedule(cron_schedule="0 4 11 * *", job=implnet_job_cuahsihisirwaids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisirwaids0(_context):
    run_config = {}
    return run_config
