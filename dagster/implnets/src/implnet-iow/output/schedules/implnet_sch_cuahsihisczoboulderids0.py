from dagster import schedule

from jobs.implnet_jobs_cuahsihisczoboulderids0 import implnet_job_cuahsihisczoboulderids0

@schedule(cron_schedule="0 9 * * 5", job=implnet_job_cuahsihisczoboulderids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisczoboulderids0(_context):
    run_config = {}
    return run_config
