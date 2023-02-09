from dagster import schedule

from jobs.implnet_jobs_cuahsi125 import implnet_job_cuahsi125

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi125, execution_timezone="US/Central")
def implnet_sch_cuahsi125(_context):
    run_config = {}
    return run_config
