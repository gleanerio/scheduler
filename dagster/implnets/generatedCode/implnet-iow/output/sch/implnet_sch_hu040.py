from dagster import schedule

from jobs.implnet_jobs_hu040 import implnet_job_hu040

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_hu040, execution_timezone="US/Central")
def implnet_sch_hu040(_context):
    run_config = {}
    return run_config
