from dagster import schedule

from jobs.implnet_jobs_cuahsi174 import implnet_job_cuahsi174

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_cuahsi174, execution_timezone="US/Central")
def implnet_sch_cuahsi174(_context):
    run_config = {}
    return run_config
