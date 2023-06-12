from dagster import schedule

from jobs.implnet_jobs_norway import implnet_job_norway

@schedule(cron_schedule="0 3 * * 3", job=implnet_job_norway, execution_timezone="US/Central")
def implnet_sch_norway(_context):
    run_config = {}
    return run_config
