from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__14 import implnet_job_wade_wade__14

@schedule(cron_schedule="0 9 17 * *", job=implnet_job_wade_wade__14, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__14(_context):
    run_config = {}
    return run_config
