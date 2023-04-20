from dagster import schedule

from jobs.implnet_jobs_pucdp import implnet_job_pucdp

@schedule(cron_schedule="0 3 * * 6", job=implnet_job_pucdp, execution_timezone="US/Central")
def implnet_sch_pucdp(_context):
    run_config = {}
    return run_config
