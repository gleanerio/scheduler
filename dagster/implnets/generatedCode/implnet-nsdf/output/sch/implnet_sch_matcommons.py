from dagster import schedule

from jobs.implnet_jobs_matcommons import implnet_job_matcommons

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_matcommons, execution_timezone="US/Central")
def implnet_sch_matcommons(_context):
    run_config = {}
    return run_config
