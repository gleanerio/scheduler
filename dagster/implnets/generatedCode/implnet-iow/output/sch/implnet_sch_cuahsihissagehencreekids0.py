from dagster import schedule

from jobs.implnet_jobs_cuahsihissagehencreekids0 import implnet_job_cuahsihissagehencreekids0

@schedule(cron_schedule="0 0 17 * *", job=implnet_job_cuahsihissagehencreekids0, execution_timezone="US/Central")
def implnet_sch_cuahsihissagehencreekids0(_context):
    run_config = {}
    return run_config
