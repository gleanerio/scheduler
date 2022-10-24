from dagster import schedule

from jobs.implnet_jobs_iow35 import implnet_job_iow35

@schedule(cron_schedule="0 11 * * 0", job=implnet_job_iow35, execution_timezone="US/Central")
def implnet_sch_iow35(_context):
    run_config = {}
    return run_config
