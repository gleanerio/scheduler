from dagster import schedule

from jobs.implnet_jobs_iow38 import implnet_job_iow38

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_iow38, execution_timezone="US/Central")
def implnet_sch_iow38(_context):
    run_config = {}
    return run_config
