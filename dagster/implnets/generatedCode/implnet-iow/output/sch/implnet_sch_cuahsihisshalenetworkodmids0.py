from dagster import schedule

from jobs.implnet_jobs_cuahsihisshalenetworkodmids0 import implnet_job_cuahsihisshalenetworkodmids0

@schedule(cron_schedule="0 20 12 * *", job=implnet_job_cuahsihisshalenetworkodmids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisshalenetworkodmids0(_context):
    run_config = {}
    return run_config
