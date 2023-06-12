from dagster import schedule

from jobs.implnet_jobs_cuahsihisczocatalinaids0 import implnet_job_cuahsihisczocatalinaids0

@schedule(cron_schedule="0 12 * * 3", job=implnet_job_cuahsihisczocatalinaids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisczocatalinaids0(_context):
    run_config = {}
    return run_config
