from dagster import schedule

from jobs.implnet_jobs_usapdc import implnet_job_usapdc

@schedule(cron_schedule="0 0 7 * *", job=implnet_job_usapdc, execution_timezone="US/Central")
def implnet_sch_usapdc(_context):
    run_config = {}
    return run_config
