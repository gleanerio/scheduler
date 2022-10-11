from dagster import schedule

from jobs.implnet_jobs_cuahsi133 import implnet_job_cuahsi133

@schedule(cron_schedule="0 17 * * 0", job=implnet_job_cuahsi133, execution_timezone="US/Central")
def implnet_sch_cuahsi133(_context):
    run_config = {}
    return run_config