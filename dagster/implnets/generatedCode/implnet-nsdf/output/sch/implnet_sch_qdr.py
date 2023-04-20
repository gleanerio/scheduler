from dagster import schedule

from jobs.implnet_jobs_qdr import implnet_job_qdr

@schedule(cron_schedule="0 6 * * 6", job=implnet_job_qdr, execution_timezone="US/Central")
def implnet_sch_qdr(_context):
    run_config = {}
    return run_config
