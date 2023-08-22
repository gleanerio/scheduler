from dagster import schedule

from jobs.implnet_jobs_r2r import implnet_job_r2r

@schedule(cron_schedule="0 6 6 * *", job=implnet_job_r2r, execution_timezone="US/Central")
def implnet_sch_r2r(_context):
    run_config = {}
    return run_config
