from dagster import schedule

from jobs.implnet_jobs_aws import implnet_job_aws

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_aws, execution_timezone="US/Central")
def implnet_sch_aws(_context):
    run_config = {}
    return run_config
