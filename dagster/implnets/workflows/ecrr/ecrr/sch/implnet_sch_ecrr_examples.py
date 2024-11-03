from dagster import schedule

from ..jobs.implnet_jobs_ecrr_examples import job_ecrr_examples

@schedule(cron_schedule="0 16 5 * *", job=job_ecrr_examples, execution_timezone="US/Central")
def implnet_sch_ecrr_examples(_context):
    run_config = {}
    return run_config
