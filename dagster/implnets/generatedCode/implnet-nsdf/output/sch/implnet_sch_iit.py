from dagster import schedule

from jobs.implnet_jobs_iit import implnet_job_iit

@schedule(cron_schedule="0 18 * * 4", job=implnet_job_iit, execution_timezone="US/Central")
def implnet_sch_iit(_context):
    run_config = {}
    return run_config
