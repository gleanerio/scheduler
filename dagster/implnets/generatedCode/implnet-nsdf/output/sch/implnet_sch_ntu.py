from dagster import schedule

from jobs.implnet_jobs_ntu import implnet_job_ntu

@schedule(cron_schedule="0 6 * * 3", job=implnet_job_ntu, execution_timezone="US/Central")
def implnet_sch_ntu(_context):
    run_config = {}
    return run_config
