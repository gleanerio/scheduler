from dagster import schedule

from jobs.implnet_jobs_cuahsihisnewnids0 import implnet_job_cuahsihisnewnids0

@schedule(cron_schedule="0 6 * * 1", job=implnet_job_cuahsihisnewnids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisnewnids0(_context):
    run_config = {}
    return run_config
