from dagster import schedule

from jobs.implnet_jobs_gfv11pois0 import implnet_job_gfv11pois0

@schedule(cron_schedule="0 6 * * 4", job=implnet_job_gfv11pois0, execution_timezone="US/Central")
def implnet_sch_gfv11pois0(_context):
    run_config = {}
    return run_config
