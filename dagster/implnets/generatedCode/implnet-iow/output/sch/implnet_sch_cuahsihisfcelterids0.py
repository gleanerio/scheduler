from dagster import schedule

from jobs.implnet_jobs_cuahsihisfcelterids0 import implnet_job_cuahsihisfcelterids0

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_cuahsihisfcelterids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisfcelterids0(_context):
    run_config = {}
    return run_config
