from dagster import schedule

from jobs.implnet_jobs_cuahsihisandrewsforestlterids0 import implnet_job_cuahsihisandrewsforestlterids0

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_cuahsihisandrewsforestlterids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisandrewsforestlterids0(_context):
    run_config = {}
    return run_config
