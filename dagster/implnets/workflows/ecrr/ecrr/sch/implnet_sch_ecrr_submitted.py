from dagster import schedule

from ..jobs.implnet_jobs_ecrr_submitted import job_ecrr_submitted

@schedule(cron_schedule="0 8 3 * *", job=job_ecrr_submitted, execution_timezone="US/Central")
def implnet_sch_ecrr_submitted(_context):
    run_config = {}
    return run_config
