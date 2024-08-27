from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_cuahsihisshalenetworkodmids1 import implnet_job_cuahsihisshalenetworkodmids1

@schedule(cron_schedule="0 4 17 * *", job=implnet_job_cuahsihisshalenetworkodmids1, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_cuahsihisshalenetworkodmids1(_context):
    run_config = {}
    return run_config