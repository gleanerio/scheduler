from dagster import schedule

from jobs.implnet_jobs_ref59 import implnet_job_ref59

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_ref59, execution_timezone="US/Central")
def implnet_sch_ref59(_context):
    run_config = {}
    return run_config
