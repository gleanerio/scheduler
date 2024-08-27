from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_cuahsicuahsihislczoodm2ids0 import implnet_job_cuahsicuahsihislczoodm2ids0

@schedule(cron_schedule="0 20 2 * *", job=implnet_job_cuahsicuahsihislczoodm2ids0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_cuahsicuahsihislczoodm2ids0(_context):
    run_config = {}
    return run_config
