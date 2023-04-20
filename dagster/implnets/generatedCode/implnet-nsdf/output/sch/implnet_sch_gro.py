from dagster import schedule

from jobs.implnet_jobs_gro import implnet_job_gro

@schedule(cron_schedule="0 12 * * 3", job=implnet_job_gro, execution_timezone="US/Central")
def implnet_sch_gro(_context):
    run_config = {}
    return run_config
