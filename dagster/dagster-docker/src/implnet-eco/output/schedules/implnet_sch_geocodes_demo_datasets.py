from dagster import schedule

from jobs.implnet_jobs_geocodes_demo_datasets import implnet_job_geocodes_demo_datasets

@schedule(cron_schedule="0 15 * * 5", job=implnet_job_geocodes_demo_datasets, execution_timezone="US/Central")
def implnet_sch_geocodes_demo_datasets(_context):
    run_config = {}
    return run_config
