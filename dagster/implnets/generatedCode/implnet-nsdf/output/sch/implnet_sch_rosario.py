from dagster import schedule

from jobs.implnet_jobs_rosario import implnet_job_rosario

@schedule(cron_schedule="0 12 * * 6", job=implnet_job_rosario, execution_timezone="US/Central")
def implnet_sch_rosario(_context):
    run_config = {}
    return run_config
