from dagster import schedule

from jobs.implnet_jobs_cuahsihispanolaodmids0 import implnet_job_cuahsihispanolaodmids0

@schedule(cron_schedule="0 20 11 * *", job=implnet_job_cuahsihispanolaodmids0, execution_timezone="US/Central")
def implnet_sch_cuahsihispanolaodmids0(_context):
    run_config = {}
    return run_config
