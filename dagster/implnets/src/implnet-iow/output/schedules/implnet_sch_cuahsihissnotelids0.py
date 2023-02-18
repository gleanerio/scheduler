from dagster import schedule

from jobs.implnet_jobs_cuahsihissnotelids0 import implnet_job_cuahsihissnotelids0

@schedule(cron_schedule="0 12 * * 6", job=implnet_job_cuahsihissnotelids0, execution_timezone="US/Central")
def implnet_sch_cuahsihissnotelids0(_context):
    run_config = {}
    return run_config
