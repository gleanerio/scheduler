from dagster import schedule

from jobs.implnet_jobs_hopkins import implnet_job_hopkins

@schedule(cron_schedule="0 21 * * 4", job=implnet_job_hopkins, execution_timezone="US/Central")
def implnet_sch_hopkins(_context):
    run_config = {}
    return run_config
