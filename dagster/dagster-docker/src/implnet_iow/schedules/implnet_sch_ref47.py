from dagster import schedule

from jobs.implnet_jobs_ref47 import implnet_job_ref47

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_ref47, execution_timezone="US/Central")
def implnet_sch_ref47(_context):
    run_config = {}
    return run_config
