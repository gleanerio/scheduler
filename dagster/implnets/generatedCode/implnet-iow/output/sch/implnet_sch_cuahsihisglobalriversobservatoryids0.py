from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_cuahsihisglobalriversobservatoryids0 import implnet_job_cuahsihisglobalriversobservatoryids0

@schedule(cron_schedule="0 0 6 * *", job=implnet_job_cuahsihisglobalriversobservatoryids0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_cuahsihisglobalriversobservatoryids0(_context):
    run_config = {}
    return run_config
