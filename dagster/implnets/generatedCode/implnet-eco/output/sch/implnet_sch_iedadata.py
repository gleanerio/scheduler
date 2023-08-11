from dagster import schedule

from jobs.implnet_jobs_iedadata import implnet_job_iedadata

@schedule(cron_schedule="0 2 3 * *", job=implnet_job_iedadata, execution_timezone="US/Central")
def implnet_sch_iedadata(_context):
    run_config = {}
    return run_config
