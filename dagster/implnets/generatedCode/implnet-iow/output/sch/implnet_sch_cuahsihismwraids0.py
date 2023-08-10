from dagster import schedule

from jobs.implnet_jobs_cuahsihismwraids0 import implnet_job_cuahsihismwraids0

@schedule(cron_schedule="0 20 13 * *", job=implnet_job_cuahsihismwraids0, execution_timezone="US/Central")
def implnet_sch_cuahsihismwraids0(_context):
    run_config = {}
    return run_config
