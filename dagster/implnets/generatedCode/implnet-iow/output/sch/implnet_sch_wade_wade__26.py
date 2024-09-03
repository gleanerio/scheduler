from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__26 import implnet_job_wade_wade__26

@schedule(cron_schedule="0 9 15 * *", job=implnet_job_wade_wade__26, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__26(_context):
    run_config = {}
    return run_config
