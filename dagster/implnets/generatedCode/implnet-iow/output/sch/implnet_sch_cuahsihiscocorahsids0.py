from dagster import schedule

from jobs.implnet_jobs_cuahsihiscocorahsids0 import implnet_job_cuahsihiscocorahsids0

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_cuahsihiscocorahsids0, execution_timezone="US/Central")
def implnet_sch_cuahsihiscocorahsids0(_context):
    run_config = {}
    return run_config
