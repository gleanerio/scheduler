from dagster import schedule

from jobs.implnet_jobs_unidata import implnet_job_unidata

@schedule(cron_schedule="0 15 1 * *", job=implnet_job_unidata, execution_timezone="US/Central")
def implnet_sch_unidata(_context):
    run_config = {}
    return run_config
