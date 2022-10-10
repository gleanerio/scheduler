from dagster import schedule

from jobs.implnet_jobs_iow36 import implnet_job_iow36

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_iow36, execution_timezone="US/Central")
def implnet_sch_iow36(_context):
    run_config = {}
    return run_config
