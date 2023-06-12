from dagster import schedule

from jobs.implnet_jobs_netherland import implnet_job_netherland

@schedule(cron_schedule="0 0 * * 3", job=implnet_job_netherland, execution_timezone="US/Central")
def implnet_sch_netherland(_context):
    run_config = {}
    return run_config
