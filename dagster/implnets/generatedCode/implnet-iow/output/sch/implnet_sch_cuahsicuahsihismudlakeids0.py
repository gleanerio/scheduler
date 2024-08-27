from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_cuahsicuahsihismudlakeids0 import implnet_job_cuahsicuahsihismudlakeids0

@schedule(cron_schedule="0 4 3 * *", job=implnet_job_cuahsicuahsihismudlakeids0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_cuahsicuahsihismudlakeids0(_context):
    run_config = {}
    return run_config
