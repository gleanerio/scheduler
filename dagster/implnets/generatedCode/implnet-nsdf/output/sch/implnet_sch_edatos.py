from dagster import schedule

from jobs.implnet_jobs_edatos import implnet_job_edatos

@schedule(cron_schedule="0 21 * * 2", job=implnet_job_edatos, execution_timezone="US/Central")
def implnet_sch_edatos(_context):
    run_config = {}
    return run_config
