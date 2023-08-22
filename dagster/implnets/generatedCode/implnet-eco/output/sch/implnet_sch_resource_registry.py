from dagster import schedule

from jobs.implnet_jobs_resource_registry import implnet_job_resource_registry

@schedule(cron_schedule="0 12 6 * *", job=implnet_job_resource_registry, execution_timezone="US/Central")
def implnet_sch_resource_registry(_context):
    run_config = {}
    return run_config
