from dagster import schedule

from jobs.implnet_jobs_cuahsihisgleondorsetids0 import implnet_job_cuahsihisgleondorsetids0

@schedule(cron_schedule="0 8 10 * *", job=implnet_job_cuahsihisgleondorsetids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisgleondorsetids0(_context):
    run_config = {}
    return run_config
