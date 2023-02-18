from dagster import schedule

from jobs.implnet_jobs_cuahsihisloganriverids0 import implnet_job_cuahsihisloganriverids0

@schedule(cron_schedule="0 0 * * 4", job=implnet_job_cuahsihisloganriverids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisloganriverids0(_context):
    run_config = {}
    return run_config
