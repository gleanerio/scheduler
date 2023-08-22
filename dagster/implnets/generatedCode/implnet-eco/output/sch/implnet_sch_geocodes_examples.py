from dagster import schedule

from jobs.implnet_jobs_geocodes_examples import implnet_job_geocodes_examples

@schedule(cron_schedule="0 12 3 * *", job=implnet_job_geocodes_examples, execution_timezone="US/Central")
def implnet_sch_geocodes_examples(_context):
    run_config = {}
    return run_config
