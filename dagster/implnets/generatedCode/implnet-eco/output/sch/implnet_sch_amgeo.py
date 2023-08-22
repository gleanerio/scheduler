from dagster import schedule

from jobs.implnet_jobs_amgeo import implnet_job_amgeo

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_amgeo, execution_timezone="US/Central")
def implnet_sch_amgeo(_context):
    run_config = {}
    return run_config
