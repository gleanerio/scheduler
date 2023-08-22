from dagster import schedule

from jobs.implnet_jobs_cuahsihisnashrwaids0 import implnet_job_cuahsihisnashrwaids0

@schedule(cron_schedule="0 0 16 * *", job=implnet_job_cuahsihisnashrwaids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisnashrwaids0(_context):
    run_config = {}
    return run_config
