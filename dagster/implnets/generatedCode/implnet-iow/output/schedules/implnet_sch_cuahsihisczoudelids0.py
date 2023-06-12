from dagster import schedule

from jobs.implnet_jobs_cuahsihisczoudelids0 import implnet_job_cuahsihisczoudelids0

@schedule(cron_schedule="0 9 * * 1", job=implnet_job_cuahsihisczoudelids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisczoudelids0(_context):
    run_config = {}
    return run_config
