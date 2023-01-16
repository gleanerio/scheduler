from dagster import schedule

from jobs.implnet_jobs_resourceregistry import implnet_job_resourceregistry

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_resourceregistry, execution_timezone="US/Central")
def implnet_sch_resourceregistry(_context):
    run_config = {}
    return run_config
