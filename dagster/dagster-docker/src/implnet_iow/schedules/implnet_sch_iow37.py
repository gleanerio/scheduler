from dagster import schedule

from jobs.implnet_jobs_iow37 import implnet_job_iow37

@schedule(cron_schedule="0 13 * * 0", job=implnet_job_iow37, execution_timezone="US/Central")
def implnet_sch_iow37(_context):
    run_config = {}
    return run_config
