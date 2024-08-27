from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_cuahsihishydrodataczhrids0 import implnet_job_cuahsihishydrodataczhrids0

@schedule(cron_schedule="0 4 7 * *", job=implnet_job_cuahsihishydrodataczhrids0, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_cuahsihishydrodataczhrids0(_context):
    run_config = {}
    return run_config