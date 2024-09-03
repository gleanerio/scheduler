from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_wade_wade__32 import implnet_job_wade_wade__32

@schedule(cron_schedule="0 6 13 * *", job=implnet_job_wade_wade__32, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_wade_wade__32(_context):
    run_config = {}
    return run_config
