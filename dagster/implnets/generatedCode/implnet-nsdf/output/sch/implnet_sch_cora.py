from dagster import schedule

from jobs.implnet_jobs_cora import implnet_job_cora

@schedule(cron_schedule="0 0 * * 2", job=implnet_job_cora, execution_timezone="US/Central")
def implnet_sch_cora(_context):
    run_config = {}
    return run_config
