from dagster import schedule

from jobs.implnet_jobs_cuahsihismuddyriverids0 import implnet_job_cuahsihismuddyriverids0

@schedule(cron_schedule="0 12 8 * *", job=implnet_job_cuahsihismuddyriverids0, execution_timezone="US/Central")
def implnet_sch_cuahsihismuddyriverids0(_context):
    run_config = {}
    return run_config
