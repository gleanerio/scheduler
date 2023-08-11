from dagster import schedule

from jobs.implnet_jobs_ecrr_examples import implnet_job_ecrr_examples

@schedule(cron_schedule="0 1 7 * *", job=implnet_job_ecrr_examples, execution_timezone="US/Central")
def implnet_sch_ecrr_examples(_context):
    run_config = {}
    return run_config
