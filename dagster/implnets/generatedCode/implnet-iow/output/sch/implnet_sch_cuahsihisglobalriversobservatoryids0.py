from dagster import schedule

from jobs.implnet_jobs_cuahsihisglobalriversobservatoryids0 import implnet_job_cuahsihisglobalriversobservatoryids0

@schedule(cron_schedule="0 16 7 * *", job=implnet_job_cuahsihisglobalriversobservatoryids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisglobalriversobservatoryids0(_context):
    run_config = {}
    return run_config
