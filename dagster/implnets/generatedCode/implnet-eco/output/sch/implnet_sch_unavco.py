from dagster import schedule

from jobs.implnet_jobs_unavco import implnet_job_unavco

@schedule(cron_schedule="0 18 * * 2", job=implnet_job_unavco, execution_timezone="US/Central")
def implnet_sch_unavco(_context):
    run_config = {}
    return run_config
